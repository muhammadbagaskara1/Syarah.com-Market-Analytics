# %%
import pandas as pd

df = pd.read_csv('UsedCarsSA_Unclean_EN.csv', delimiter=';', encoding='utf-8')

# %%
# Convert price to numeric, "Negotiable" becomes NaN
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Make sure Negotiable is boolean (True/False)
df["Negotiable"] = df["Negotiable"].astype(bool)

print(df[["Price", "Negotiable"]].head(10))


# %%
from sqlalchemy import create_engine

username = "root"      # default MySQL user
password = "SQL123#"   # set your root password here
host = "localhost"     # since running locally
port = 3306            # default MySQL port
database = "SyarahListingDB"

# Create SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")



# %%
# Step 3.1: Get unique values from "Make"
unique_makes = df["Make"].dropna().unique()
dim_make = pd.DataFrame({"make_name": unique_makes})

# Step 3.2: Insert into dim_make table
dim_make.to_sql("dim_make", engine, if_exists="append", index=False)

print("✅ dim_make inserted")


# %%
unique_types = df["Type"].dropna().unique()
dim_type = pd.DataFrame({"type_name": unique_types})
dim_type.to_sql("dim_type", engine, if_exists="append", index=False)

print("✅ dim_type inserted")


# %%
# Origin
unique_origins = df["Origin"].dropna().unique()
dim_origin = pd.DataFrame({"origin_name": unique_origins})
dim_origin.to_sql("dim_origin", engine, if_exists="append", index=False)
print("✅ dim_origin inserted")

# %%
# Color
unique_colors = df["Color"].dropna().unique()
dim_color = pd.DataFrame({"color_name": unique_colors})
dim_color.to_sql("dim_color", engine, if_exists="append", index=False)
print("✅ dim_color inserted")

# %%
# Options
unique_options = df["Options"].dropna().unique()
dim_options = pd.DataFrame({"options_name": unique_options})
dim_options.to_sql("dim_options", engine, if_exists="append", index=False)
print("✅ dim_options inserted")

# %%
# Fuel Type
unique_fuels = df["Fuel_Type"].dropna().unique()
dim_fuel = pd.DataFrame({"fuel_type": unique_fuels})
dim_fuel.to_sql("dim_fuel", engine, if_exists="append", index=False)
print("✅ dim_fuel inserted")

# %%
# Gear Type
unique_gears = df["Gear_Type"].dropna().unique()
dim_gear = pd.DataFrame({"gear_type": unique_gears})
dim_gear.to_sql("dim_gear", engine, if_exists="append", index=False)
print("✅ dim_gear inserted")

# %%
# Condition
unique_conditions = df["Condition"].dropna().unique()
dim_condition = pd.DataFrame({"condition_type": unique_conditions})
dim_condition.to_sql("dim_condition", engine, if_exists="append", index=False)
print("✅ dim_condition inserted")

# %%
# Region
unique_regions = df["Region"].dropna().unique()
dim_region = pd.DataFrame({"region_name": unique_regions})
dim_region.to_sql("dim_region", engine, if_exists="append", index=False)
print("✅ dim_region inserted")

# %%
# Make a copy so original df is untouched
df_fact = df.copy()


# %%
# Load dimension tables from MySQL into pandas
dim_make = pd.read_sql("SELECT * FROM dim_make", engine)
dim_type = pd.read_sql("SELECT * FROM dim_type", engine)
dim_origin = pd.read_sql("SELECT * FROM dim_origin", engine)
dim_color = pd.read_sql("SELECT * FROM dim_color", engine)
dim_options = pd.read_sql("SELECT * FROM dim_options", engine)
dim_fuel = pd.read_sql("SELECT * FROM dim_fuel", engine)
dim_gear = pd.read_sql("SELECT * FROM dim_gear", engine)
dim_condition = pd.read_sql("SELECT * FROM dim_condition", engine)
dim_region = pd.read_sql("SELECT * FROM dim_region", engine)


# %%
# Merge with make_id
df_fact = df_fact.merge(dim_make, left_on="Make", right_on="make_name", how="left")

# Merge with type_id
df_fact = df_fact.merge(dim_type, left_on="Type", right_on="type_name", how="left")

# Merge with origin_id
df_fact = df_fact.merge(dim_origin, left_on="Origin", right_on="origin_name", how="left")

# Merge with color_id
df_fact = df_fact.merge(dim_color, left_on="Color", right_on="color_name", how="left")

# Merge with options_id
df_fact = df_fact.merge(dim_options, left_on="Options", right_on="options_name", how="left")

# Merge with fuel_id
df_fact = df_fact.merge(dim_fuel, left_on="Fuel_Type", right_on="fuel_type", how="left")

# Merge with gear_id
df_fact = df_fact.merge(dim_gear, left_on="Gear_Type", right_on="gear_type", how="left")

# Merge with condition_id
df_fact = df_fact.merge(dim_condition, left_on="Condition", right_on="condition_type", how="left")

# Merge with region_id
df_fact = df_fact.merge(dim_region, left_on="Region", right_on="region_name", how="left")


# %%
# Keep only fact table columns
fact_df = df_fact[[
    "Link", "Year", "Engine_Size", "Mileage", "Price", "Negotiable",
    "make_id", "type_id", "origin_id", "color_id", "options_id",
    "fuel_id", "gear_id", "condition_id", "region_id"
]]


# %%
fact_df.head()

# %%
# Load into fact_listing
fact_df.to_sql("fact_listing", engine, if_exists="append", index=False)

print("✅ Fact table loaded into MySQL!")



