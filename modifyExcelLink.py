import pandas as pd

# Assuming your Excel file has a column named 'Links' that contains these URLs
excel_file_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/PythonDeveloperScrapeData.xlsx'
df = pd.read_excel(excel_file_path)

# Function to remove extra words after '?'
def remove_extra_words(url):
    if '?' in url:
        return url.split('?')[0]
    else:
        return url

# Apply the function to the 'Links' column
df['Profile Link'] = df['Profile Link'].apply(remove_extra_words)

# Save the updated DataFrame to a new Excel file or overwrite the existing one
df.to_excel('C:/Users/Dell/Documents/UiPath/Python Developer/ModifyProfileLinkfile.xlsx', index=False)
