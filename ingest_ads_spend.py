# ingest_ads_spend.py
import pandas as pd
from datetime import datetime
import duckdb
import sys

# Parameters (for n8n, pass as arguments)
csv_path = sys.argv[1] if len(sys.argv) > 1 else "ads_spend.csv"
print(f"Using CSV path: {csv_path}")
source_file_name = csv_path.split("/")[-1]

# Read CSV
df = pd.read_csv(csv_path)

# Add provenance
df["load_date"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
df["source_file_name"] = source_file_name

# Write to DuckDB
con = duckdb.connect("warehouse.duckdb")
con.execute("""
CREATE TABLE IF NOT EXISTS ads_spend (
    date DATE,
    platform VARCHAR,
    account VARCHAR,
    campaign VARCHAR,
    country VARCHAR,
    device VARCHAR,
    spend DOUBLE,
    clicks INTEGER,
    impressions INTEGER,
    conversions INTEGER,
    load_date TIMESTAMP,
    source_file_name VARCHAR
)
""")
con.execute("INSERT INTO ads_spend SELECT * FROM df")
con.close()
print("Ingestion complete.")