import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('datset.csv')

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Handle missing values (if any)
# For example, fill missing values in 'Units_Sold' with the mean
if df['Units_Sold'].isnull().sum() > 0:
    df['Units_Sold'].fillna(df['Units_Sold'].mean(), inplace=True)

# Check for duplicates
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Ensure data types are correct
print("\nData types before conversion:")
print(df.dtypes)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convert 'Store_ID', 'Product_ID', 'Units_Sold', and 'Promotion' to integers
df['Store_ID'] = df['Store_ID'].astype(int)
df['Product_ID'] = df['Product_ID'].astype(int)
df['Units_Sold'] = df['Units_Sold'].astype(int)
df['Promotion'] = df['Promotion'].astype(int)

# Convert 'Channel' and 'Region' to categorical types
df['Channel'] = df['Channel'].astype('category')
df['Region'] = df['Region'].astype('category')

print("\nData types after conversion:")
print(df.dtypes)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_synthetic_sales_data.csv', index=False)

print("\nCleaned DataFrame saved to 'cleaned_synthetic_sales_data.csv'.")
