import pandas as pd 
#Show all columns and rows when printing dataframes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
excel_path="/Users/tasia/Documents/Carbon_Emissions_Project/National_Fossil_Carbon_Emissions_2025_v0.3.xlsx"
df=pd.read_excel(excel_path, engine="openpyxl")
#Gathering stats on the data set
print(df.head())
print(df.columns)
print(df.head(20))
print("Number of NaN values in each column:")
print(df.isnull().sum())
#Cleaning the data set by removing rows with NaN values
df_cleaned=df.dropna()
print("Number of NaN values in each column after cleaning:")
print(df_cleaned.isnull().sum())
print(df_cleaned.head())
print(df_cleaned.dtypes)
#convert data types from object to numeric for analysis
df_cleaned=df_cleaned.apply(pd.to_numeric, errors='ignore')
print(df_cleaned.dtypes)
#Look at stats after converting data types
print(df_cleaned.describe())
#Drop first column Unnamed:0
df_cleaned=df_cleaned.drop(columns=['Unnamed: 0'])
#Calculate the country with the highest average fossil carbon emissions
highest_avg_emissions=df_cleaned.mean().idxmax()
print("The country with the highest average fossil carbon emissions is:", highest_avg_emissions)
#Drop the column titled world 
df_cleaned=df_cleaned.drop(columns=['World'])
#Calculate the country with the highest average fossil carbon emissions after dropping world column
highest_avg_emissions=df_cleaned.mean().idxmax()
print("The country with the highest average fossil carbon emissions after dropping World column is:", highest_avg_emissions)
#Print the value of the mean of Non-OECD
print("The value of the mean for Non-OECD:", df_cleaned['Non-OECD'].mean())
#Drop statistical diffefence columns
df_cleaned=df_cleaned.drop(columns=['Statistical Difference'])
#Calculate the country with the lowest average fossil carbon emissions
lowest_avg_emissions=df_cleaned.mean().idxmin()
print("The country with the lowest average fossil carbon emissions is:", lowest_avg_emissions)
#Print the value of the mean of NIUE
print("The value of the mean for NIUE:", df_cleaned['NIUE'].mean())