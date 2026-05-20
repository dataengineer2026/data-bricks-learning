-- ============================================================
-- Unity Catalog Setup for Weather Lakehouse Project
-- ============================================================
-- This script creates the required catalog, schema, and volume
-- for storing weather data in a medallion architecture.
-- 
-- Run this ONCE before executing the bronze_ingest script.
-- ============================================================

-- 1. Create the Catalog
CREATE CATALOG IF NOT EXISTS lakehouse_projects
COMMENT 'Catalog for all lakehouse data projects';

-- 2. Create the Weather Schema
CREATE SCHEMA IF NOT EXISTS lakehouse_projects.weather
COMMENT 'Schema for weather data pipeline (Bronze/Silver/Gold layers)';

-- 3. Create the Volume for file storage
CREATE VOLUME IF NOT EXISTS lakehouse_projects.weather.weather_data
COMMENT 'Volume for storing raw weather data files in Delta format';

-- ============================================================
-- Verification Queries
-- ============================================================

-- Show catalog details
DESCRIBE CATALOG lakehouse_projects;

-- Show schema details
DESCRIBE SCHEMA lakehouse_projects.weather;

-- Show volume details
DESCRIBE VOLUME lakehouse_projects.weather.weather_data;

-- List all volumes in the schema
SHOW VOLUMES IN lakehouse_projects.weather;

-- ============================================================
-- Expected Volume Path:
-- /Volumes/lakehouse_projects/weather/weather_data
-- 
-- Subdirectories will be created automatically by the ingestion script:
--   - /Volumes/lakehouse_projects/weather/weather_data/bronze
--   - /Volumes/lakehouse_projects/weather/weather_data/silver
--   - /Volumes/lakehouse_projects/weather/weather_data/gold
-- ============================================================
