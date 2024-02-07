# import pandas as pd

# # Assuming your Excel file has a column named 'Links' that contains these URLs
# excel_file_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/RemoveDuplicateSheet.xlsx'
# df = pd.read_excel(excel_file_path, header=None)

# # Access the 'Profile Link' column by index
# profile_link_index = 2  # Assuming 'Profile Link' is the third column (index 2)
# profile_link_column = df.iloc[:, profile_link_index]

# # Function to remove extra words after '?'
# def remove_extra_words(url):
#     if '?' in url:
#         return url.split('?')[0]
#     else:
#         return url

# # Apply the function to the 'Profile Link' column
# df.iloc[:, profile_link_index] = df.iloc[:, profile_link_index].apply(remove_extra_words)

# # Save the updated DataFrame to a new Excel file or overwrite the existing one
# df.to_excel('C:/Users/Dell/Documents/UiPath/Python Developer/RemoveDuplicateSheet.xlsx', index=False, header=None)

import pandas as pd

def remove_extra_words_from_column(excel_file_path):
    print('dddddd')

    column_index=2

    # Read Excel file without headers
    df = pd.read_excel(excel_file_path, header=None)

    # Check if the specified index is within the valid range
    if column_index < df.shape[1]:
        # Access the specified column by index
        column_to_modify = df.iloc[:, column_index]

        # Function to remove extra words after '?'
        def remove_extra_words(url):
            if '?' in url:
                return url.split('?')[0]
            else:
                return url

        # Apply the function to the specified column
        df.iloc[:, column_index] = column_to_modify.apply(remove_extra_words)

        # Save the updated DataFrame to the same Excel file
        df.to_excel(excel_file_path, index=False, header=None)
    else:
        print("Invalid column index. Please check the number of columns in your DataFrame.")

    return "Modify the excel"

# Example usage
#excel_file_path = 'C:/Users/Dell/Documents/UiPath/Python Developer/SortedSheet.xlsx'
#column_index_to_modify = 2  # Assuming 'Profile Link' is the third column (index 2)
#remove_extra_words_from_column(excel_file_path)
