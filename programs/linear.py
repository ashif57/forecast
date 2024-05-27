import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('cleaned_synthetic_sales_data.csv')

# Ensure 'Date' column is of datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Extract features
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Month'] = df['Date'].dt.month
df['DayOfYear'] = df['Date'].dt.dayofyear

# Create the target variable 'Price'
df['Price'] = df['Revenue'] / df['Units_Sold']

# Remove any rows with NaN values
df.dropna(subset=['Price'], inplace=True)

# Define features and target variable
features = ['DayOfWeek', 'Month', 'DayOfYear']
X = df[features]
y = df['Price']

# Split data into training and testing sets
train_size = int(0.8 * len(df))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Fit linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Evaluate the model
train_rmse = np.sqrt(mean_squared_error(y_train, train_predictions))
test_rmse = np.sqrt(mean_squared_error(y_test, test_predictions))
print(f'Train RMSE: {train_rmse}')
print(f'Test RMSE: {test_rmse}')

# Forecast future prices (next 30 days)
last_date = df['Date'].iloc[-1]
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=30)
future_features = pd.DataFrame({
    'DayOfWeek': future_dates.dayofweek,
    'Month': future_dates.month,
    'DayOfYear': future_dates.dayofyear
})
future_predictions = model.predict(future_features)

# Create a DataFrame for the forecasted data
forecast_df = pd.DataFrame({'Date': future_dates, 'Forecasted_Price': future_predictions})

# Visualize the results
plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Price'], label='Actual Price', marker='o')
plt.plot(df['Date'].iloc[train_size:], test_predictions, label='Test Predictions', marker='o')
plt.plot(forecast_df['Date'], forecast_df['Forecasted_Price'], label='Forecasted Price', marker='o', color='red')
plt.title('Price Forecast with Linear Regression')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
