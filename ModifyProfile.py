import pandas as pd
import requests
from bs4 import BeautifulSoup

def read_profile_links_excel(file_path):
    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)

        # Check if "Profile Link" column exists in the DataFrame
        if "Profile Link" not in df.columns:
            raise ValueError("The 'Profile Link' column is not present in the Excel file.")

        # Iterate through each row of the "Profile Link" column
        for index, profile_link in enumerate(df["Profile Link"]):
            print(f"Row {index + 2}: {profile_link}")  # Adding 2 because index starts from 0, and Excel row numbers start from 2
            try:
                # Send a GET request to the profile link and retrieve the HTML content
                response = requests.get(profile_link)
                response.raise_for_status()  # Raise an exception for bad responses

                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the <main> tag with class name "scaffold-layout__main"
                main_tag = soup.find('main', class_='scaffold-layout__main')

                # Check if the main_tag is found
                if main_tag:
                # Print the content of the <main> tag
                    print(f"Content of <main> tag for row {index + 2}:\n{main_tag.prettify()}")
                else:
                    print(f"<main> tag with class name 'scaffold-layout__main' not found for row {index + 2}")
                    
            except requests.exceptions.RequestException as req_err:
                print(f"Error retrieving HTML content for row {index + 2}: {str(req_err)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'your_excel_file.xlsx' with the actual path to your Excel file
excel_file_path = './ModifyProfileLinkfile.xlsx'
read_profile_links_excel(excel_file_path)
