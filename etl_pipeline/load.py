
def get_postgres_engine():
    '''
    constructs a SQLalchemy engine object for postgres DB from .env file

    parameter: None

    Returns: 
     - sqlalchemy engine (sqlalchemy.engine.Engine)
    '''
    user = os.getenv('pg_user')
    password = os.getenv('pg_password')
    host = os.getenv('pg_host')
    port = os.getenv('pg_port')
    dbname = os.getenv('pg_dbname')
    connection_string = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
    engine = create_engine(connection_string)
    return engine


## Additional postgres engine for macOS 

def get_postgres_engine2():
    # Use URL object to create connection string
    connection_url = URL(
        drivername="postgresql+psycopg2",
        username=os.getenv('pg_user'),
        password=os.getenv('pg_password'),
        host=os.getenv('pg_host'),
        port=os.getenv('pg_port'),
        database=os.getenv('pg_dbname')
    )
    # Create engine
    engine = create_engine(connection_url)
    return engine

# snowflake connection 

def get_snowflake_engine():

