import os
import requests

def fetch_data(url, staging_dir):
    file_name = url.split('/')[-1]
    file_path = os.path.join(staging_dir, file_name)

    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded data from {url} to {file_path}")
        return file_path
    else:
        print(f"Failed to download data from {url}")
        return None

def fetch_all_data(urls, staging_dir):

    for url in urls:
        fetch_data(url, staging_dir)



# using pandas 
'''
def download_data(url, staging_dir):
    # os.makedirs(staging_dir, exist_ok=True)
    
    file_name = url.split('/')[-1]
    file_path = f"{staging_dir}/{file_name}"  # Using f-string for constructing the file path
    
    try:
        # Read CSV data from URL into DataFrame with error handling for bad lines
        df = pd.read_csv(url, on_bad_lines='warn')  # Use 'skip' if you want to silently skip bad lines
        # Save DataFrame to CSV
        df.to_csv(file_path, index=False)
        print(f"Downloaded data from {url} to {file_path}")
        return file_path
    except Exception as e:
        print(f"Failed to download data from {url}: {e}")
        return None

def download_all_data(urls, staging_dir):
    for url in urls:
        download_data(url, staging_dir)

#########################################################################################################

'''