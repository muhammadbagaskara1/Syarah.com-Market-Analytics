# get_raw_data.py

import pandas as pd
from sqlalchemy import create_engine

def get_data():
    """
    Connects to MySQL and returns fact_listing joined with all dimension tables.
    """
    # 1. Database connection parameters
    user = "root"
    password = "SQL123#"
    host = "localhost"  # or your DB host
    port = 3306
    database = "SyarahListingDB"

    # 2. Create connection string
    connection_str = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_str)

    # 3. Define query to join fact table with all dimension tables
    query = """
    SELECT f.listing_id,
           f.year,
           f.engine_size,
           f.mileage,
           f.price,
           f.negotiable,
           m.make_name,
           t.type_name,
           o.origin_name,
           c.color_name,
           opt.options_name,
           g.gear_type,
           fu.fuel_type,
           co.condition_type,
           r.region_name
    FROM fact_listing f
    LEFT JOIN dim_make m ON f.make_id = m.make_id
    LEFT JOIN dim_type t ON f.type_id = t.type_id
    LEFT JOIN dim_origin o ON f.origin_id = o.origin_id
    LEFT JOIN dim_color c ON f.color_id = c.color_id
    LEFT JOIN dim_options opt ON f.options_id = opt.options_id
    LEFT JOIN dim_gear g ON f.gear_id = g.gear_id
    LEFT JOIN dim_fuel fu ON f.fuel_id = fu.fuel_id
    LEFT JOIN dim_condition co ON f.condition_id = co.condition_id
    LEFT JOIN dim_region r ON f.region_id = r.region_id;
    """

    # 4. Execute query and return DataFrame
    df = pd.read_sql(query, engine)
    return df

# Optional: allow script to run standalone
if __name__ == "__main__":
    df = get_data()
    print("Data fetched successfully!")
    print(df.head())
