-- Create Database
CREATE DATABASE IF NOT EXISTS SyarahListingDB;
USE SyarahListingDB;

-- Dimension Tables
CREATE TABLE dim_make (
    make_id INT AUTO_INCREMENT PRIMARY KEY,
    make_name VARCHAR(100) UNIQUE
);

CREATE TABLE dim_type (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(100) UNIQUE
);

CREATE TABLE dim_origin (
    origin_id INT AUTO_INCREMENT PRIMARY KEY,
    origin_name VARCHAR(100) UNIQUE
);

CREATE TABLE dim_color (
    color_id INT AUTO_INCREMENT PRIMARY KEY,
    color_name VARCHAR(50) UNIQUE
);

CREATE TABLE dim_options (
    options_id INT AUTO_INCREMENT PRIMARY KEY,
    options_name VARCHAR(50) UNIQUE
);

CREATE TABLE dim_fuel (
    fuel_id INT AUTO_INCREMENT PRIMARY KEY,
    fuel_type VARCHAR(50) UNIQUE
);

CREATE TABLE dim_gear (
    gear_id INT AUTO_INCREMENT PRIMARY KEY,
    gear_type VARCHAR(50) UNIQUE
);

CREATE TABLE dim_condition (
    condition_id INT AUTO_INCREMENT PRIMARY KEY,
    condition_type VARCHAR(50) UNIQUE
);

CREATE TABLE dim_region (
    region_id INT AUTO_INCREMENT PRIMARY KEY,
    region_name VARCHAR(100) UNIQUE
);

-- Fact Table
CREATE TABLE fact_listing (
    listing_id INT AUTO_INCREMENT PRIMARY KEY,
    link VARCHAR(1000),
    year INT,
    engine_size FLOAT,
    mileage BIGINT,
    price DECIMAL(15,2),
    negotiable BOOLEAN,

    -- Foreign Keys
    make_id INT,
    type_id INT,
    origin_id INT,
    color_id INT,
    options_id INT,
    fuel_id INT,
    gear_id INT,
    condition_id INT,
    region_id INT,

    FOREIGN KEY (make_id) REFERENCES dim_make(make_id),
    FOREIGN KEY (type_id) REFERENCES dim_type(type_id),
    FOREIGN KEY (origin_id) REFERENCES dim_origin(origin_id),
    FOREIGN KEY (color_id) REFERENCES dim_color(color_id),
    FOREIGN KEY (options_id) REFERENCES dim_options(options_id),
    FOREIGN KEY (fuel_id) REFERENCES dim_fuel(fuel_id),
    FOREIGN KEY (gear_id) REFERENCES dim_gear(gear_id),
    FOREIGN KEY (condition_id) REFERENCES dim_condition(condition_id),
    FOREIGN KEY (region_id) REFERENCES dim_region(region_id)
);
