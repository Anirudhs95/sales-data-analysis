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

# Average Sales
avg_sales = data['Sales'].mean()

# Sales by Product
groupby_product = data.groupby('Product')['Sales'].sum()

# Sales by Category
groupby_category = data.groupby('Category')['Sales'].sum()

# Visualization
# Bar Chart (Sales by Product – Matplotlib)
groupby_product.plot(kind='bar')
plt.title('Total Sales by product')
plt.xlabel('Products')
plt.ylabel('Sales amount')
plt.show()

# Bar Plot (Sales by Category – Seaborn)
sns.barplot(x=groupby_category.index, y=groupby_category.values)
plt.title("Total Sales by category")
plt.show()
