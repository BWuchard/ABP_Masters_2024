from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def read_matrix_from_file(file_path, columns_to_read):
    # Read specific columns from the file
    matrix = np.loadtxt(file_path, usecols=columns_to_read, skiprows=1, delimiter=',')
    # Reshape matrix to make it a 2D array
    return np.reshape(matrix, (1, -1))

# Read specific columns from files
columns_to_read = [4, 5, 6, 7, 8]

# List to store cosine similarities
cos_sim_list = []

# Open the text files containing matrices
with open('CoverageProcPlans.txt', 'r') as file1, open('GNIProcPlans.txt', 'r') as file2:
    # Iterate through each line in both files simultaneously
    for line1, line2 in zip(file1, file2):
        # Strip whitespace and check if the line is empty
        line1 = line1.strip()
        line2 = line2.strip()
        if not line1 or not line2:
            continue

        # Extract file paths from lines
        file_path1 = line1
        file_path2 = line2

        # Read matrices from the corresponding files
        matrix1 = read_matrix_from_file(file_path1, columns_to_read)
        matrix2 = read_matrix_from_file(file_path2, columns_to_read)

        # Calculate cosine similarity for each pair of matrices
        cos_sim = cosine_similarity(matrix1, matrix2)

        # Append cosine similarity to the list
        cos_sim_list.append(cos_sim[0][0])

# Convert the list of cosine similarities into a matrix
cos_sim_matrix = np.array(cos_sim_list).reshape(-1, 1)

print("Cosine Similarity Matrix:")
print(cos_sim_matrix)
