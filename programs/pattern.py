import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned CSV file into a DataFrame
df = pd.read_csv('cleaned_synthetic_sales_data.csv')

# Ensure 'Date' column is of datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate data by date to find daily sales trends
daily_sales = df.groupby('Date').agg({'Revenue': 'sum', 'Units_Sold': 'sum'}).reset_index()

# Plot daily revenue trend
plt.figure(figsize=(14, 7))
plt.plot(daily_sales['Date'], daily_sales['Revenue'], marker='o', linestyle='-')
plt.title('Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

# Aggregate data by month to find monthly sales trends
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month').agg({'Revenue': 'sum', 'Units_Sold': 'sum'}).reset_index()
monthly_sales['Month'] = monthly_sales['Month'].dt.to_timestamp()

# Plot monthly revenue trend
plt.figure(figsize=(14, 7))
plt.plot(monthly_sales['Month'], monthly_sales['Revenue'], marker='o', linestyle='-')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()

# Aggregate data by channel to compare physical vs online sales
channel_sales = df.groupby(['Date', 'Channel']).agg({'Revenue': 'sum', 'Units_Sold': 'sum'}).reset_index()

# Plot revenue trend by channel
plt.figure(figsize=(14, 7))
for channel in channel_sales['Channel'].unique():
    channel_data = channel_sales[channel_sales['Channel'] == channel]
    plt.plot(channel_data['Date'], channel_data['Revenue'], marker='o', linestyle='-', label=channel)
plt.title('Daily Revenue Trend by Channel')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.legend()
plt.grid(True)
plt.show()

# Aggregate data by region to compare regional sales trends
region_sales = df.groupby(['Date', 'Region']).agg({'Revenue': 'sum', 'Units_Sold': 'sum'}).reset_index()

# Plot revenue trend by region
plt.figure(figsize=(14, 7))
for region in region_sales['Region'].unique():
    region_data = region_sales[region_sales['Region'] == region]
    plt.plot(region_data['Date'], region_data['Revenue'], marker='o', linestyle='-', label=region)
plt.title('Daily Revenue Trend by Region')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.legend()
plt.grid(True)
plt.show()
