import os
from bs4 import BeautifulSoup
import pandas as pd

# Replace with the path to your folder
folder_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/HiringManager/'

# Replace with path to your existing Excel file
excel_file_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/Data Engineer.xlsx'

# Read data from each text file in a folder
def read_text_file(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        data = file.read()
    return data

def main():
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        files = sorted(files, key=lambda x: int(os.path.splitext(x)[0]))

        if not files:
            print("No text files found in the folder.")
            return

        # Initialize an empty list to store data for the DataFrame
        data_list = []

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            html_content = read_text_file(file_path)
            print(f"Data from {file_name}")

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the <main> tag with class "scaffold-layout__main"
            main_element = soup.find('main', class_='scaffold-layout__main')

            if main_element:
                # Find the <div> with class "job-view-layout jobs-details" inside the <main> element
                job_details_div = main_element.find('div', class_='job-view-layout jobs-details')

                if job_details_div:
                    # Find the <div> with class "mh4 pt4 pb3" inside the job_details_div
                    target_div = job_details_div.find('div', class_='mh4 pt4 pb3')

                    if target_div:
                        # Find the <a> tag with class "app-aware-link" inside the target_div
                        link_element = target_div.find('a', class_='app-aware-link')

                        if link_element:
                            # Extract the href attribute
                            href_attribute = link_element.get('href')
                            print(f"href attribute value: {href_attribute}")

                            # Append the href attribute value to the data_list
                            data_list.append({'ManagerLink': href_attribute})

                        else:
                            print("No <a> tag with class 'app-aware-link' found inside target_div.")
                            data_list.append({'ManagerLink': ''})

                    else:
                        print("No <div> with class 'mh4 pt4 pb3' found inside job_details_div.")
                        data_list.append({'ManagerLink': ''})

                else:
                    print("No <div> with class 'job-view-layout jobs-details' found inside <main>.")
                    data_list.append({'ManagerLink': ''})

            else:
                print("No <main> tag with class 'scaffold-layout__main' found.")
                data_list.append({'ManagerLink': ''})

        # Read the existing Excel file into a DataFrame
        existing_df = pd.read_excel(excel_file_path)

        # Create a DataFrame from the data_list
        df = pd.DataFrame(data_list)

        # Add the "ManagerLink" column to the existing DataFrame
        existing_df['ManagerLink'] = df['ManagerLink']

        # Save the modified DataFrame to the existing Excel file
        existing_df.to_excel(excel_file_path, index=False)

        print(f"{len(data_list)} ManagerLink values added to the Excel file.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
