def save_csv(file_path, content):
    with open(file_path, 'wb') as file:
        file.write(content)
