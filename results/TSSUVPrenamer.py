import os
import pandas as pd

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# Iterate over files in the directory
for filename in os.listdir(current_directory):
    if filename.startswith('TSS') and filename.endswith('.csv'):
        filepath = os.path.join(current_directory, filename)
        
        # Read the CSV file
        df = pd.read_csv(filepath)
        
        # Update the 'ExpName' column
        df[' ExpName[i]'] = 'TSS' + df[' ExpName[i]'].astype(str)
        
        # Write the updated DataFrame back to the CSV file
        df.to_csv(filepath, index=False)
        
        print(f"Updated file: {filename}")
