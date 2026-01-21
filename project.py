import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load & Explore Data
data = pd.read_csv("day-13/sales_data.csv",encoding='latin1')
print(data.head())
print(data.info())

# Data Cleaning
print(data.isnull().sum())

# Analysis Using Pandas
# Total Sales
total_sales = data['Sales'].sum()
print("Total sales:",total_sales)

# Average Sales
avg_sales = data['Sales'].mean()
print("Average sales:",avg_sales)

# Sales by Product
by_product = data.groupby('Product')['Sales'].sum()
print(by_product)

# Sales by Category
by_category = data.groupby('Category')['Sales'].sum()
print(by_category)

# Visualization
# Bar Chart (Sales by Product – Matplotlib)
by_product.plot(kind='bar')
plt.title('Sales by product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Bar Plot (Sales by Category – Seaborn)
sns.barplot(x=by_category.index, y=by_category.values)
plt.title("Sales by category")
plt.show()