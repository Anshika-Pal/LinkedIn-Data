import os
from bs4 import BeautifulSoup

def read_text_files(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"The path '{folder_path}' is not a directory.")
        return

    # Get a list of all files in the directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Filter only text files
    text_files = [f for f in files if f.lower().endswith(".txt")]

    if not text_files:
        print(f"No text files found in the directory '{folder_path}'.")
        return

    # Read and print the content of each text file
    for file_name in text_files:
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')

            # Find div tags with the specified class
            target_divs = soup.find_all('div', class_='pv-profile-section__section-info section-info')

            # Do something with the found divs, e.g., print their content
            for div in target_divs:
                print(f"Content of div in {file_name}:\n{div}")
                print("=========================================")
           

# Provide the path to the folder containing text files
folder_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/HiringManager/ContactInfo/'
read_text_files(folder_path)
