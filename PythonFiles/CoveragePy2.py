import pandas as pd

# Load the Excel file into a dataframe
file_path = "91_Country_Reference_data.csv"
df = pd.read_csv(file_path)

# List of countries to filter
gavi_countries = sorted(["Afghanistan", "Benin", "Burkina Faso", "Burundi", "Cambodia", "CAR", "Chad", "Comoros", "DRC", "Eritrea", "Ethiopia", "Gambia", "Guinea", "Guinea-Bissau", "Haiti", "Kyrgyzstan", "Lesotho", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania", "Mozambique", "Myanmar", "Nepal", "Niger", "North Korea", "Rwanda", "Senegal", "Sierra Leone", "Somalia", "South Sudan", "Sudan", "Syria", "Tajikistan", "Tanzania", "Togo", "Uganda", "Yemen", "Zambia", "Zimbabwe", "Bangladesh", "Cameroon", "Congo", "Côte d'Ivoire", "Djibouti", "Ghana", "Kenya", "Laos", "Nigeria", "Pakistan", "Papua New Guinea", "São Tomé", "Solomon Isl."])

# Filter the dataframe to keep only the desired countries
df_filtered = df[df["Country"].isin(gavi_countries)]

# Extract only the "Country" column
filtered_countries = df_filtered["Country"].tolist()

# Print out countries in the list not found in the dataframe
countries_not_found = [country for country in gavi_countries if country not in filtered_countries]
print("Countries not found in the dataframe:")
for country in countries_not_found:
    print(country)

# Extract only the "Country" and "Population" columns
desired_columns = ["Country", "Population "]
df_subset = df_filtered[desired_columns]

# Remove duplicate entries based on the "Country" column
df_subset_no_duplicates = df_subset.drop_duplicates(subset=["Country"])

# Display the resulting dataframe
print(df_subset_no_duplicates)
# Load the "averagecoverages.xlsx" file
coverages_file_path = "averagecoverages.xlsx"
df_coverages = pd.read_excel(coverages_file_path)

# Merge the filtered dataframe with the coverages dataframe on the "Country" column
merged_df = pd.merge(df_subset_no_duplicates, df_coverages, on="Country")

# Multiply the "Population" values with the "Coverage" values
merged_df["Coverage * Population "] = merged_df["Population "] * merged_df["Coverage"]

# Display the resulting dataframe
print(merged_df)
