import os
os.environ["WORDCLOUD_FONT_PATH"] = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

import pandas as pd
from ydata_profiling import ProfileReport

# Load the dataset safely
df = pd.read_csv("DataHut_AT_Dm_PriceExtractions_20250624.CSV", sep="|", engine="python", on_bad_lines="skip")
df.columns = df.columns.str.strip()

# Define only relevant columns
columns = [
    "unique_id", "competitor_name", "extraction_date", "product_name", "grammage_quantity", "grammage_unit",
    "regular_price", "selling_price", "price_valid_from", "price_per_unit", "percentage_discount",
    "promotion_price", "promotion_valid_from", "promotion_valid_upto", "promotion_description",
    "currency", "breadcrumb", "pdp_url", "region", "pack_size", "site_shown_uom"
]

# Filter only existing columns
existing_cols = [col for col in columns if col in df.columns]
df = df[existing_cols]

# Handle empty or broken DataFrame
if df.empty:
    print("❌ DataFrame is empty after column selection.")
    exit()

# Fix object columns with missing values
for col in df.select_dtypes(include=["object", "category"]).columns:
    df[col] = df[col].fillna("Missing").astype(str)

# Build the profile with minimal and safe config to avoid chi-squared crash
profile = ProfileReport(
    df,
    title="QA Profile Report",
    explorative=True,
    minimal=True,  # Turns off expensive computations like interactions and correlations
)

profile.to_file("qa_profile_report.html")
print("✅ Report saved as qa_profile_report.html")
