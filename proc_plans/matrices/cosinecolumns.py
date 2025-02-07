import pandas as pd
import numpy as np

# Read the Excel file into a DataFrame
df = pd.read_excel('4marketcosinesimilarity.xlsx', header=None)

# Convert DataFrame to numpy array
matrix = df.values.astype(float)

# Get the upper triangular indices (excluding the diagonal)
indices = np.triu_indices(matrix.shape[0], k=1)

# Extract the values and their corresponding indices
values = matrix[indices]
indices_i, indices_j = indices

# Create a DataFrame for the result
result_df = pd.DataFrame({'Position': [f"{i}-{j}" for i, j in zip(indices_i + 1, indices_j + 1)],
                          'Value': values})

# Save the result to an Excel file
result_df.to_excel('result.xlsx', index=False)
