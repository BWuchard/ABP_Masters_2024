from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def read_matrix_from_file(file_path, columns_to_read):
    # Read specific columns from the file
    matrix = np.loadtxt(file_path, usecols=columns_to_read, skiprows=1, delimiter=',')
    # Reshape matrix to make it a 2D array
    return np.reshape(matrix, (1, -1))

# Define the columns to read from the CSV files
columns_to_read = [4, 5, 6, 7, 8]

# Open the text files containing matrices
with open('4ProcPlan1.txt', 'r') as file1, open('4ProcPlan2.txt', 'r') as file2:
    # Read the entire contents of the files
    matrix1_list = [read_matrix_from_file(line.strip(), columns_to_read) for line in file1 if line.strip()]
    matrix2_list = [read_matrix_from_file(line.strip(), columns_to_read) for line in file2 if line.strip()]

# Calculate cosine similarity for each pair of vectors
cos_sim_matrix = np.zeros((len(matrix1_list), len(matrix2_list)))
for i, matrix1 in enumerate(matrix1_list):
    for j, matrix2 in enumerate(matrix2_list):
        cos_sim = cosine_similarity(matrix1, matrix2)
        cos_sim_matrix[i, j] = cos_sim[0][0]

print("Cosine Similarity Matrix:")
print(cos_sim_matrix)
