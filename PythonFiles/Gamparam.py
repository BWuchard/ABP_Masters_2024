import pandas as pd

# Define the lists and sort them alphabetically
Gavi = sorted(["Afghanistan", "Benin", "Burkina Faso", "Burundi", "Cambodia", "CAR", "Chad", "Comoros", "DRC", "Eritrea", "Ethiopia", "Gambia", "Guinea", "Guinea-Bissau", "Haiti", "Kyrgyzstan", "Lesotho", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania", "Mozambique", "Myanmar", "Nepal", "Niger", "North Korea", "Rwanda", "Senegal", "Sierra Leone", "Somalia", "South Sudan", "Sudan", "Syria", "Tajikistan", "Tanzania", "Togo", "Uganda", "Yemen", "Zambia", "Zimbabwe", "Bangladesh", "Cameroon", "Congo", "Côte d'Ivoire", "Djibouti", "Ghana", "Kenya", "Laos", "Nigeria", "Pakistan", "Papua New Guinea", "São Tomé", "Solomon Isl."])
antigens = sorted(['BCG', 'DT', 'DTP', 'HepB', 'Hib', 'HPV', 'IPV', 'MMR', 'PCV', 'Rota', 'Td', 'Varicella', 'YF', 'OPV'])

# Define the file path
file_path = 'Gamparam.xlsx'

# Read the Excel file
xl = pd.ExcelFile(file_path)

# Specify the sheet name
sheet_name = 'DALYs All ages'

# Read the specified sheet into a DataFrame
df = xl.parse(sheet_name)

# Define the renaming dictionary
renaming_dict = {
    'Democratic Republic of the Congo': 'DRC',
    'Central African Republic':'CAR',
    "Democratic People's Republic of Korea": 'North Korea',
    'Syrian Arab Republic': 'Syria',
    'United Republic of Tanzania': 'Tanzania',
    "Lao People's Democratic Republic": 'Laos',
    'Sao Tome and Principe': 'São Tomé',
    'Solomon Islands': 'Solomon Isl.'
}

# Rename columns
df.rename(columns=renaming_dict, inplace=True)

# Find columns missing from the DataFrame that should be in the Gavi list
missing_columns = [country for country in Gavi if country not in df.columns]

# Filter the DataFrame to include only columns for Gavi countries
filtered_df = df[df.columns[df.columns.isin(Gavi)]]

# Print the filtered DataFrame
print("Gavi Countries in DataFrame:")
print(filtered_df)

# Print Gavi countries not found in the DataFrame
print("\nColumns missing from DataFrame that should be in Gavi list:")
print(missing_columns)

# Define a dictionary of antigen-disease associations
antigen_disease = {
    'BCG': 'Tuberculosis',
    'DT': 'Diphtheria and Tetanus',
    'DTP': 'Diphtheria and Tetanus and Whooping Cough',
    'HepB': 'Acute hepatitis B',
    'Hib': 'Meningitis and infectious disease',
    'HPV': 'Cervic uteri cancer and other STDs',
    'IPV': 'Upper respiratory',
    'MMR': 'Measles',
    'PCV': 'Infectious disease',
    'Rota': 'Diarrhoeal',
    'Td': 'Tetanus and Diphtheria',
    'Varicella': 'Infectious disease',
    'YF': 'Yellow fever',
    'OPV': 'Upper respiratory'
}

# Create an empty dictionary to store antigen-specific rows
antigen_rows = {}

# Iterate through each antigen
for antigen in antigens:
    # Create an empty list to store rows for the current antigen
    antigen_rows[antigen] = []
    
    # Iterate through each word associated with the current antigen
    for word in antigen_disease[antigen].split(' and '):
        # Filter rows containing the word in the GHE cause column
        antigen_rows[antigen].append(df[df['GHE cause'].str.contains(word, case=False)])

# Print the rows for each antigen
for antigen, rows in antigen_rows.items():
    print(f"Rows for {antigen}:")
    print(pd.concat(rows))
    print()

    # Create an empty dictionary to store summed rows for each antigen
summed_antigen_rows = {}

# Iterate through each antigen
for antigen, rows in antigen_rows.items():
    # Concatenate all the filtered rows and sum along the columns
    summed_row = pd.concat(rows).sum()
    
    # Assign the summed row to the antigen name
    summed_antigen_rows[antigen] = summed_row

# Convert the dictionary of summed rows into a DataFrame
summed_antigen_df = pd.DataFrame(summed_antigen_rows)

# Transpose the DataFrame so that antigens become columns
summed_antigen_df = summed_antigen_df.T

# Drop the 'GHE cause' column
summed_antigen_df.drop(columns=['GHE cause'], inplace=True)

# Print the DataFrame with summed rows for each antigen
print("DataFrame with summed rows for each antigen:")
print(summed_antigen_df)

# Convert all values to numeric
summed_antigen_df = summed_antigen_df.apply(pd.to_numeric, errors='coerce')

# Fill missing values in each column with the column average
summed_antigen_df = summed_antigen_df.apply(lambda col: col.fillna(col.mean()))

# Print the DataFrame with missing values filled with column averages
print("DataFrame with missing values filled with column averages:")
print(summed_antigen_df)

# Filter the DataFrame to include only columns for Gavi countries
filtered_df = summed_antigen_df[summed_antigen_df.columns[summed_antigen_df.columns.isin(Gavi)]]
print(filtered_df)


