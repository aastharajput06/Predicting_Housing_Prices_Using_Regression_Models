import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset from the data folder
data = pd.read_csv('data/housing.csv')

# Basic exploration
print(data.head())        # First 5 rows
print(data.info())        # Data types, missing values
print(data.describe())    # Stats like mean, min, maxexit()

# Plot 1: Histogram of house prices
plt.hist(data['median_house_value'], bins=50)
plt.title('Distribution of House Prices')
plt.xlabel('Price (USD)')
plt.ylabel('Frequency')
plt.savefig('price_histogram.png')  # Save to housing_project/
plt.show()

# Plot 2: Scatter plot of income vs. price
plt.scatter(data['median_income'], data['median_house_value'], alpha=0.1)
plt.title('House Price vs. Median Income')
plt.xlabel('Median Income (tens of thousands USD)')
plt.ylabel('House Price (USD)')
plt.savefig('income_vs_price.png')  # Save to housing_project/
plt.show()