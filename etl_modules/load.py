import pandas as pd
from utils.db import get_postgres_engine

def load_to_postgres(output_dir, table_name):
    df = pd.read_csv(output_dir)
    engine = get_postgres_engine()
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"{len(df)} rows of data successfully loaded to PostgreSQL table '{table_name}'")