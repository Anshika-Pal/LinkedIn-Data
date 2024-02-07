import os
import pandas as pd
from bs4 import BeautifulSoup
import re  # Import the regular expressions module

# Replace 'your_folder_path' with the actual path of the folder containing text files
folder_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/HiringManager/'

# Save the DataFrame to an Excel file
excel_file_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/Data Engineer.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# List all files in the folder
file_list = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# Define a regular expression pattern for extracting email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Example regular expression for matching phone numbers
phone_number_pattern = re.compile(
    r'''
    # Match optional international dialing code
    (?:(?:\+|00)\d{1,4}\s*)?
    
    # Match optional opening parenthesis
    (?:\(\d{1,}\)\s*)?
    
    # Match digits, spaces, dots, hyphens, or slashes
    (?:\d{1,}[-.\s/]?)?
    
    # Match more digits, spaces, dots, hyphens, or slashes
    (?:\d{1,}[-.\s/]?)?
    
    # Match additional digits
    \d{1,}
    ''',
    re.VERBOSE
)

# Iterate through each text file and read its content
for file_name in file_list:
    # Initialize an empty list to store extracted h1_texts
    h1_texts=[]
    email_texts = []
    phone_texts = []  # Added list for phone numbers

    file_path = os.path.join(folder_path, file_name)

    # Open and read the content of the file with 'utf-8' encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(file_content, 'html.parser')

        # # Use BeautifulSoup to parse HTML content and find h1 tag
        h1_element = soup.find('h1', class_='text-heading-xlarge inline t-24 v-align-middle break-words')

        # # Extract h1 text or set to None if not found
        h1_text = h1_element.text if h1_element else None
        
        # # Append to the list
        h1_texts.append(h1_text)

        # Find the div with id "about" inside all section tags
        about_divs = soup.find_all('section')

        flag = True

        # Iterate over each section to find the div with id "about"
        for section in about_divs:
            about_div = section.find('div', id='about')

            # Print the content of the div with id "about"
            if about_div:
                #print(about_div)

                # Find the div with class 'display-flex ph5 pv3' inside the same section
                inner_div = section.find('div', class_='display-flex ph5 pv3')

                # Print the content of the inner div
                if inner_div:
                    #print(inner_div)

                    # Find the span tag with class 'visually-hidden' inside the inner_div
                    span_tag = inner_div.find('span', class_='visually-hidden')

                    # Print the content of the span tag
                    if span_tag:
                        span_text = span_tag.text.strip()
                       
                        # Use regular expression to find email addresses in span_text
                        email_match = re.search(email_pattern, span_text)

                        if email_match:
                            email_address = email_match.group()
                            email_texts.append(email_address)
                            print("Extracted Email Address:", email_address)

                        else:
                            email_texts.append("")
                            print("No email address found in the span_text.")
                        
                        # Use regular expression to find phone numbers in span_text
                        phone_match = re.search(phone_number_pattern, span_text)

                        if phone_match:
                            phone_number = phone_match.group()
                            phone_texts.append(phone_number)
                            print("Extracted Phone Number:", phone_number)
                        else:
                            phone_texts.append("")
                            print("No phone number found in the span_text.")

                    else:
                        print("Span tag with class 'visually-hidden' not found inside the inner_div.")
                else:
                    print("Div with class 'display-flex ph5 pv3' not found inside the same section.")
                
                flag = False
            
        if flag:
            print("Div with id 'about' not found inside a section tag.") 

    # Check if email_addresses is not empty before accessing its elements
    if  h1_texts:
        row_index = int(file_name.split(".")[0])
        print(row_index)
        df.loc[row_index, 'HR_Name'] =  h1_texts[0]
        print(df)
            
        # Check if email_addresses is not empty before accessing its elements
        if email_texts:
            row_index = int(file_name.split(".")[0])
            print(row_index)
            df.loc[row_index, 'E_Mail'] = email_texts[0]
            print(df)

    # Check if phone_texts is not empty before accessing its elements
    if phone_texts:
        row_index = int(file_name.split(".")[0])
        print(row_index)
        df.loc[row_index, 'P_No'] = phone_texts[0]
        print(df)

# # Save the updated DataFrame back to Excel
df.to_excel(excel_file_path, index=False)

print("Excel sheet updated successfully.")
