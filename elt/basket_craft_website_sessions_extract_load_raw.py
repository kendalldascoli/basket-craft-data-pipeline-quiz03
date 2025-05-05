from sqlalchemy import text

from dotenv import load_dotenv
load_dotenv()

import pandas as pd
from sqlalchemy import create_engine
import os

from dotenv import load_dotenv
load_dotenv()

# Load MySQL credentials from environment variables (set in GitHub Secrets)
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = "db.isba.co"
MYSQL_PORT = 3306
MYSQL_DB = "basket_craft"

# Create MySQL connection string
mysql_conn_str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
mysql_engine = create_engine(mysql_conn_str)

# Query for sessions in December 2023
query = '''
SELECT *
FROM website_sessions
WHERE created_at BETWEEN '2023-12-01' AND '2023-12-31 23:59:59';
'''

# Fetch data into a DataFrame
df = pd.read_sql(query, mysql_engine)

print("Rows fetched from MySQL:", len(df))
print(df.head())

# Load Postgres credentials from environment variables
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB = os.getenv("PG_DB")

# Create Postgres connection string
pg_conn_str = f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
pg_engine = create_engine(pg_conn_str)

# Truncate table before loading
with pg_engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE raw.website_sessions"))

# Load new data
df.to_sql("website_sessions", pg_engine, schema="raw", if_exists="append", index=False)

