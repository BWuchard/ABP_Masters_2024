import pandas as pd

# Read the Excel file
file_path = 'All_results.xlsx'
df = pd.read_excel(file_path)

# Group by 'ExpName', 'n_market', and 'Test', and calculate the average of 'TPF', 'TSS', and 'TCS'
df['TPF'] = df.groupby(['ExpName', 'n_markets', 'Test'])['TPF'].transform('mean')
df['TSS'] = df.groupby(['ExpName', 'n_markets', 'Test'])['TSS'].transform('mean')
df['TCS'] = df.groupby(['ExpName', 'n_markets', 'Test'])['TCS'].transform('mean')

# Drop duplicate rows to keep only one row per unique 'ExpName', 'n_market', and 'Test' combination
df.drop_duplicates(subset=['ExpName', 'n_markets', 'Test'], inplace=True)

# Reorder columns if needed
df = df[['ExpName', 'n_markets', 'Test', 'TPF', 'TSS', 'TCS']]

# Save the result to a new Excel file or overwrite the original file
df.to_excel('output_excel_file.xlsx', index=False)
