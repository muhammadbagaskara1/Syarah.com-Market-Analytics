# Syarah.com-Market-Analytics
Syarah.com market analytics to determine used car price factors

Syarah Listing Market Analytics

A full Data Engineering + Data Analysis project using a Saudi Arabian used cars dataset.
This project demonstrates ETL processes, star schema design, Python-based preprocessing & EDA, and integration with MySQL for Tableau visualization.

Project Structure
Syarah Listing Market Analytics/
│
├─ SyarahListing.ipynb           # Initial exploration of raw CSV, column understanding, minor preprocessing
├─ Create_Database_SyarahListing.sql  # MySQL script to create database & star schema
├─ load_data_to_sql.py           # Script to load raw CSV data into MySQL
├─ get_raw_data.py               # Script to fetch data from MySQL for analysis/EDA
├─ get_raw_data_clean.py         # (Optional) Script to push cleaned data to MySQL
├─ EDA.ipynb                     # Python notebook for preprocessing, feature engineering, and EDA
└─ requirements.txt              # Python dependencies for the project

![ERD Diagram]([ERD.png](https://github.com/muhammadbagaskara1/Syarah.com-Market-Analytics/blob/main/SyarahListingERD.png))

Workflow / How to Run

Database Setup

Run Create_Database_SyarahListing.sql in MySQL to create the database and tables (star schema).

Load Raw Data to MySQL

Run load_data_to_sql.py to push the raw CSV data into the MySQL tables.

Clean & Prepare Data

Open EDA.ipynb to:

Preprocess raw data

Handle missing values & outliers

Feature engineering

Visualizations for analysis

Push Cleaned Data (Optional)

Run get_raw_data_clean.py to save the cleaned DataFrame into MySQL as fact_listing_clean.

This can then be connected directly to Tableau for dashboards.

Fetch Data for Analysis

Use get_raw_data.py in notebooks or scripts to fetch joined data from MySQL for further analysis.

Python Dependencies

Install the necessary packages via:

pip install -r requirements.txt


requirements.txt content:

pandas
numpy
matplotlib
seaborn
sqlalchemy
PyMySQL

Key Skills Demonstrated

Data Engineering

Designing and implementing a star schema in MySQL

ETL workflow from CSV → MySQL → Python → Tableau

Handling foreign key relationships and dimension tables

Python Data Analysis

Pandas for preprocessing, cleaning, and feature engineering

Seaborn & Matplotlib for exploratory data analysis (EDA)

Visualization

Tableau-ready data in MySQL (fact tables + joined tables)

Version Control / Portfolio Readiness

Organized folder structure with scripts and notebooks

requirements.txt for reproducibility

ERD (optional) to visualize database design

Optional Enhancements

Add ERD diagram exported from MySQL Workbench (.png or .pdf) for visual representation of schema.

Include sample dashboards from Tableau using fact_listing_clean.

Automate scripts using Shell commands / Git Bash to simulate real-world data pipeline workflow.

ERD Suggestion

You can generate an ERD from MySQL Workbench:

Open MySQL Workbench → Database → Reverse Engineer → select SyarahListingDB.

Export the resulting diagram as PNG/PDF → include in your repo.
