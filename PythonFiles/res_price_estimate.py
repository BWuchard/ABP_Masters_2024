PAHO = ['Brazil', 'Mexico', 'Bahamas', 'Barbados', 'Trinidad', 'Chile', 'Uruguay', 'St. Kitts and Nevis', 'Antigua', 'Venezuela', 'Argentina', 'Panama', 'Suriname', 'Costa Rica', 'Grenada', 'Colombia', 'Saint Lucia', 'Dominica', 'Saint Vincent', 'Cuba', 'Peru', 'Dominican Rep.', 'Ecuador', 'Jamaica', 'Belize', 'El Salvador', 'Guyana', 'Paraguay', 'Guatemala', 'Bolivia', 'Honduras', 'Nicaragua', 'Haiti']

PAHOUSC = ['Brazil', 'Mexico', 'Bahamas', 'Barbados', 'Trinidad', 'Chile', 'Uruguay', 'St. Kitts and Nevis', 'Antigua', 'Venezuela', 'Argentina', 'Panama', 'Suriname', 'Costa Rica', 'Grenada', 'Colombia', 'Saint Lucia', 'Dominica', 'Saint Vincent', 'Cuba', 'Peru', 'Dominican Rep.', 'Ecuador', 'Jamaica', 'Belize', 'El Salvador', 'Guyana', 'Paraguay', 'Guatemala', 'Bolivia', 'Honduras', 'Nicaragua', 'Haiti', 'USA', 'Canada']
user_input = input("Enter coordinating entity or list of countries:")

if user_input == 'PAHO':
    selected_list = PAHO
elif user_input == 'PAHOUSC':
    selected_list = PAHOUSC
else:
    print("Not working yet")
    
import pandas as pd

df = pd.read_csv('C:\\Users\\Bailey\\Downloads\\11_2021_Country_Status_(Server)_data.csv')

filtered_df = df[df['Country Name'].isin(selected_list)]
filtered_df = filtered_df.drop(columns=['WHO Region','Current WB Status','Gavi Eligibility', 'Gavi Co-financing'])
filtered_df = filtered_df.rename(columns={'Country Name' : 'Country', 'Birth Cohort ' : 'Annual_births', 'GDP per capita' : 'GNI_pc'})
df_sorted = filtered_df.sort_values(by='Country')
df_sorted = df_sorted.reset_index(drop=True)
df_sorted['Code'] = df_sorted.index + 1
df_sorted = df_sorted.replace(' ','_', regex=True)

column_name = 'Code'
columns = df_sorted.columns.tolist()
columns.insert(0, columns.pop(columns.index(column_name)))
df_sorted = df_sorted.reindex(columns=columns)
print(df_sorted)



df_sorted.to_csv('C:\\Users\\Bailey\\Downloads\\Country_main_dataB.csv', sep=',', index=False)
