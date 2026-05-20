# Bronze Notebook
import requests
import json
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit, to_date

# Import configuration
from config import API_BASE_URL, LOCATIONS, WEATHER_PARAMS, BRONZE_PATH

spark = SparkSession.builder.appName("Weather_Bronze").getOrCreate()

# ── Fetch weather data from Open-Meteo ──────────────────
def fetch_weather(location: dict, params: dict) -> dict:
    payload = {
        "latitude":  location["lat"],
        "longitude": location["lon"],
        **{k: ",".join(v) if isinstance(v, list) else v 
           for k, v in params.items()}
    }
    resp = requests.get(API_BASE_URL, params=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    data["city"]        = location["city"]
    data["fetched_at"]  = datetime.utcnow().isoformat()
    return data

# ── Fetch all cities ─────────────────────────────────────
all_raw = []
for loc in LOCATIONS:
    try:
        data = fetch_weather(loc, WEATHER_PARAMS)
        all_raw.append(json.dumps(data))
        print(f"✅ Fetched: {loc['city']}")
    except Exception as e:
        print(f"❌ Failed: {loc['city']} → {e}")

# ── Write to Bronze (Delta) ──────────────────────────────
# Convert JSON strings to dictionaries for serverless compatibility
json_data = [json.loads(j) for j in all_raw]

# Create DataFrame from list of dictionaries
df_bronze = spark.createDataFrame(json_data)

df_bronze = df_bronze \
    .withColumn("ingested_at", current_timestamp()) \
    .withColumn("ingestion_date", to_date(current_timestamp()))

df_bronze.write \
    .format("delta") \
    .mode("append") \
    .partitionBy("ingestion_date") \
    .option("mergeSchema", "true") \
    .save(BRONZE_PATH)

print(f"\n✅ Bronze layer written → {BRONZE_PATH}")
print(f"   Total cities ingested: {df_bronze.count()}")
