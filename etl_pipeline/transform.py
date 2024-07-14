import os
import pandas as pd

def transform_data(file_paths):
    columns = ['Div', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
    all_data = []

    for file_path in file_paths:
        df = pd.read_csv(file_path, usecols=lambda col: col in columns)
        
        # Add 'Time' column if it doesn't exist and fill with 'unknown'
        if 'Time' not in df.columns:
            df['Time'] = 'unknown'
        
        # Transform the date column to the correct format
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y', errors='coerce')
        
        # Clean the data: drop duplicates and fill missing values
        df.drop_duplicates(inplace=True)
        df.fillna({'Time': 'unknown'}, inplace=True)
        
        all_data.append(df)
    
    transformed_data = pd.concat(all_data, ignore_index=True)
    return transformed_data

def save_transformed_data(df, transformed_data_path):
    transformed_data_path = './staging_dir/transformed_data/transformed_data.csv'
    df.to_csv(transformed_data_path, index=False)


'''
def main():
    urls = [
        "https://www.football-data.co.uk/mmz4281/1920/E0.csv",
        "https://www.football-data.co.uk/mmz4281/1920/E2.csv",
        "https://www.football-data.co.uk/mmz4281/0203/E1.csv"
    ]
    
    # Directory for staging data
    staging_dir = './staging_dir/raw_data/'
    os.makedirs(staging_dir, exist_ok=True)

    # Download files
    file_paths = []
    for url in urls:
        file_name = url.split('/')[-1]
        file_path = os.path.join(staging_dir, file_name)
        download_data(url, file_path)
        file_paths.append(file_path)

    # Transform data
    transformed_data = transform_data(file_paths)
    
    # Save transformed data
    transformed_file_path = os.path.join(staging_dir, 'transformed.csv')
    save_transformed_data(transformed_data, transformed_file_path)
    
    # Load data into database (assuming you have implemented this function)
    load_data(transformed_file_path)

if __name__ == "__main__":
    main()
'''