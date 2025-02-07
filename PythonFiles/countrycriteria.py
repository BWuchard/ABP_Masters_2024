import pandas as pd

# Define the list of countries
countries = ["Afghanistan", "Benin", "Burkina Faso", "Burundi", "Cambodia", "CAR", "Chad", "Comoros", "DRC", "Eritrea", "Ethiopia", "Gambia", "Guinea", "Guinea-Bissau", "Haiti", "Kyrgyzstan", "Lesotho", "Liberia", "Madagascar", "Malawi", "Mali", "Mauritania", "Mozambique", "Myanmar", "Nepal", "Niger", "North Korea", "Rwanda", "Senegal", "Sierra Leone", "Somalia", "South Sudan", "Sudan", "Syria", "Tajikistan", "Tanzania", "Togo", "Uganda", "Yemen", "Zambia", "Zimbabwe", "Bangladesh", "Cameroon", "Congo", "Côte d'Ivoire", "Djibouti", "Ghana", "Kenya", "Laos", "Nigeria", "Pakistan", "Papua New Guinea", "São Tomé", "Solomon Isl."]

# Sample available data for the indicators
gni_data = ["$1,950", "$2,200", "$1,720", "$710", "$4,070", "$770", "$1,970", "$2,270", "$1,030", "$1,080", "$950", "$1,620", "$2,200", "$1,610", "$780", "$1,450", "$1,380", "$710", "$1,570", "$1,290", "$2,010", "$4,460", "$1,450", "$1,430", "$1,080", "$1,130", "$1,180", "$1,770", "$3,330", "$1,770", "$660", "$4,030", "$1,410", "$2,010", "$2,080", "$1,030", "$840", "$1,450", "$2,560", "$1,320", "$600", "$1,180", "$1,630", "$740", "$1,060", "$1,860", "$2,220", "$2,190", "$2,120", "$1,650", "$2,020", "$1,010", "$2,210"]

population_density_data = [56.937, 108.978, 76.046, 418.166, 95.714, 8.403, 13.059, 454.165, 39.284, 53.658, 125.568, 209.474, 53.383, 64.361, 403.739, 33.098, 72.819, 54.161, 48.193, 212.083, 17.781, 4.691, 45.869, 91.556, 205.063, 21.529, 214.828, 275.288, 90.621, 110.216, 26.267, 11.444, 25.969, 49.913, 36.475, 90.513, 51.686, 156.429, 18.221, 155.041, 28.495, 43.324, 11.396, 91.077, 14.334, 14.221, 43.401, 80.238, 14.675, 82.711, 138.497, 90.853, 71.706, 20.257]

gini_coefficient_data = [27.8, 47.8, 35.3, 42.4, 32.1, 56.3, 43.3, 45.3, 42.3, 43.7, 34.4, 32.3, 47.8, 50.7, 59.2, 28.6, 57.9, 34.8, 42.4, 45.8, 40.1, 37.9, 47.3, 39.1, 35.7, 32.6, 43.7, 44.6, 39.3, 48.2, 45.3, 33.8, 46.6, 34.0, 35.4, 46.2, 36.0, 48.5, 51.3, 45.6, 40.5, 50.0, 43.3, 48.2, 42.8, 44.3, 35.4, 41.5, 49.0, 42.7, 57.5, 42.6]

hdi_data = [0.511, 0.545, 0.452, 0.433, 0.594, 0.526, 0.394, 0.503, 0.457, 0.440, 0.485, 0.498, 0.474, 0.455, 0.503, 0.685, 0.518, 0.499, 0.527, 0.505, 0.422, 0.520, 0.456, 0.456, 0.579, 0.603, 0.524, 0.529, 0.545, 0.510, 0.374, 0.521, 0.571, 0.574, 0.536, 0.536, 0.571, 0.471, 0.597, 0.548, 0.485, 0.519, 0.557, 0.569, 0.470, 0.555, 0.558, 0.543, 0.541, 0.607, 0.554, 0.542, 0.605]

# Create a dictionary to store the data
data = {
    "Country": countries,
    "GNI": gni_data,
    "Population Density": population_density_data,
    "Gini coefficient": gini_coefficient_data,
    "Human Development Index": hdi_data,
    "Access to Basic Services": ["Data not available"] * len(countries),
    "Infrastructure Development": ["Data not available"] * len(countries),
    "Corruption Level": ["Data not available"] * len(countries),
    "Health Expenditure": ["Data not available"] * len(countries)
}

# Create a pandas DataFrame from the data dictionary
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("criteria.xlsx", index=False)
