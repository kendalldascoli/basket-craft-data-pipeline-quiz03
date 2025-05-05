import os
from dotenv import load_dotenv

load_dotenv()

for key, value in os.environ.items():
    if key.startswith("PG_") or key == "DBT_SCHEMA":
        print(f'export {key}="{value}"')
