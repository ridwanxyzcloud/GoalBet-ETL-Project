from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2
import os


# Load postgres credentials from .env
load_dotenv(override=True)


def get_postgres_engine():
    '''
    constructs a SQLalchemy engine object for postgres DB from .env file

    parameter: None

    Returns: 
     - sqlalchemy engine (sqlalchemy.engine.Engine)
    '''
    driver = 'postgresql+psycopg2'
    user = os.getenv('pg_user')
    password = os.getenv('pg_password')
    host = os.getenv('pg_host')
    port = os.getenv('pg_port')
    dbname = os.getenv('pg_dbname')

    connection_string = f'{driver}://{user}:{password}@{host}:{port}/{dbname}'
    engine = create_engine(connection_string)
    
    return engine