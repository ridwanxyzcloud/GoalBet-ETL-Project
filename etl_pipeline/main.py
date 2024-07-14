import yaml
import os
from etl_pipeline.extract import extract_data
from etl_pipeline.transform import transform_data
from etl_pipeline.load import load_data

def main():
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    raw_data_path = config['staging_paths']['raw_data']
    transformed_data_path = config['staging_paths']['transformed_data']
    db_config = config['database']

    os.makedirs(raw_data_path, exist_ok=True)
    os.makedirs(transformed_data_path, exist_ok=True)

    for source in config['data_sources']:
        url = source['url']
        raw_file_path = extract_data(url, raw_data_path)
        transformed_file_path = transform_data(raw_file_path, transformed_data_path)
        load_data(transformed_file_path, db_config)

if __name__ == '__main__':
    main()
