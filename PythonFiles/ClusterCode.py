import os

"""
"""
os.environ['OMP_NUM_THREADS'] = '1'
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_excel('criteria.xlsx')
print(df)

x = df[['AveResPrice']].copy()

wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0, n_init=10)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

sns.set()
plt.plot(range(1, 11), wcss)
plt.title('Selecting the number of clusters using the elbow method')
plt.xlabel('Clusters')
plt.ylabel('WCSS')
plt.show()

# Create KMeans object with the optimal number of clusters
n_clusters = 3  # Replace with the optimal number of clusters from the elbow method
kmeans = KMeans(n_clusters=n_clusters, random_state=0)

# Fit KMeans to the data
kmeans.fit(x)

# Get the cluster labels for each data point
cluster_labels = kmeans.labels_

# Increment the cluster labels by 1 to start from 1 instead of 0
cluster_labels = cluster_labels + 1

# Add the cluster labels to the original dataframe
df['Cluster'] = cluster_labels

# Create a new DataFrame to store the clusters and their corresponding countries in separate columns
cluster_df = pd.DataFrame()

# Iterate through each cluster
for cluster_num in range(1, n_clusters + 1):
    # Get the countries in the current cluster
    countries_in_cluster = df[df['Cluster'] == cluster_num]['country_name'].tolist()
    
    # Create a row in the new DataFrame with the cluster number and individual country columns
    row_data = {'Cluster': cluster_num, **{f'Country_{i}': country for i, country in enumerate(countries_in_cluster, 1)}}
    cluster_df = cluster_df.append(row_data, ignore_index=True)

# Assuming you have a DataFrame called 'cluster_df'

# Specify the file name for the Excel file
output_filename = 'market_assignments_AveResPrice3.xlsx'

# Specify the sheet name you want to use
sheet_name = 'markets'

# Export the DataFrame to Excel with the specified sheet name and without the header column
with pd.ExcelWriter(output_filename) as writer:
    cluster_df.to_excel(writer, sheet_name=sheet_name, index=False, header=None)

print(f"Clustered countries saved to '{output_filename}'.")


