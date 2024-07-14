from sqlalchemy import create_engine
from dotenv import load_dotenv
import os 

load_dotenv(override=True)

def get_db_connection(db_config):

    '''
    connects to a clickhouse database using paramters from .env file

    parameter: None

    Returns: 
     - Clickhouse_connect.Client: A database client object

    '''
    engine = create_engine(f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")
    return engine
