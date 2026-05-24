# config.py / Config Notebook
# ── Locations to track ───────────────────────────────────
LOCATIONS = [
    {"city": "New York",     "lat": 40.7128,  "lon": -74.0060},
    {"city": "London",       "lat": 51.5074,  "lon": -0.1278},
    {"city": "Tokyo",        "lat": 35.6762,  "lon": 139.6503},
    {"city": "Sydney",       "lat": -33.8688, "lon": 151.2093},
    {"city": "Dubai",        "lat": 25.2048,  "lon": 55.2708},
]

# ── API Config ───────────────────────────────────────────
API_BASE_URL = "https://api.open-meteo.com/v1/forecast"
WEATHER_PARAMS = {
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "wind_speed_10m",
        "wind_direction_10m",
        "weather_code",
        "apparent_temperature",
        "uv_index"
    ],
    "daily": [
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "wind_speed_10m_max",
        "uv_index_max",
        "sunrise",
        "sunset"
    ],
    "timezone": "auto",
    "forecast_days": 7
}

# ── Storage Paths ────────────────────────────────────────
# ✅ Use Unity Catalog Volumes (create volume first)
CATALOG      = "lakehouse_projects"
SCHEMA       = "weather"
VOLUME       = "weather_data"

BASE_PATH    = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"
BRONZE_PATH  = f"{BASE_PATH}/bronze"
SILVER_PATH  = f"{BASE_PATH}/silver"
GOLD_PATH    = f"{BASE_PATH}/gold"

# ── Database ─────────────────────────────────────────────
DATABASE     = "weather_lakehouse"
