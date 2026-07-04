#!/usr/bin/env python
# coding: utf-8

# ## Exploratory Data Analysis (EDA) with the Sales Dataset using Pandas and d Matplotlib_Seaborn
#
# New notebook

# # **Exploratory Data Analysis (EDA) with the Sales Dataset using Pandas and d Matplotlib/Seaborn**
#
# ### **Objective:**
#
# The goal of this assignment is to help you apply your knowledge of Python for basic operations, Pandas for data manipulation, and Matplotlib/Seaborn for visualizations. You'll be working with a real-world dataset, and your tasks will include loading the data, performing EDA, and visualising the results.
#
# ###  **Dataset**
#
# The dataset represents transaction data from a retail business, specifically sales data for products sold in various stores. It contains multiple tables that provide insights into sales, invoices, and products. Let’s break down the tables and what they represent:
#
# #### Sales Table:
#
# InvoiceNo: The unique identifier for each invoice (or transaction).
#
# StockCode: A unique identifier for each product.
#
# Quantity: The number of units sold in each transaction.
#
# UnitPrice: The price per unit of the product.
#
# InvoiceDate: The date when the transaction occurred.
#
# #### Invoice Table:
#
# InvoiceNo: The same unique identifier for each invoice, linking the sales data with the invoice details.
#
# Country: The country where the sale was made.
#
# #### Product Table:
#
# StockCode: A unique identifier for each product.
#
# Description: The name or description of the product.
#
# Product_Category: The category the product belongs to (e.g., "Gift", "Sign", "Mug").
#
#
#
# You will need to merge them and perform the following tasks step by step.
#

# ### Task 1: Load the Excel File
# #### Objective: Import the data from the provided Excel file into Python using Pandas.
#
# Instructions:
#
# 1. Upload the provided excel file into Fabric environment
# 2. Read each sheet of the excel file as a separate dataframe.
# 3. Name the dataframe for sales as df_sales, the dataframe for invoice as df_invoice and the dataframe for product as df_product
# 4. Display the first few rows of each DataFrame to understand its structure.
#
#

# In[1]:


# Code Task Here
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# 1.Reading each sheet excel file as a separate dataframe using Pandas Library.
# reading Sales sheet from online_sales_retailer excel file as Df_sales dataframe.
df_sales = pd.read_excel(
    f"{notebookutils.nbResPath}/builtin/online_sales_retailer.xlsx", sheet_name='Sales')
# reading Invoice sheet from online_sales_retailer excel file as Df_invoice dataframe.
df_invoice = pd.read_excel(
    f"{notebookutils.nbResPath}/builtin/online_sales_retailer.xlsx", sheet_name='Invoice')
# reading Product sheet from online_sales_retailer excel file as Df_product dataframe.
df_product = pd.read_excel(
    f"{notebookutils.nbResPath}/builtin/online_sales_retailer.xlsx", sheet_name='Product')

# Display the first few rows of each DataFrame
display(df_sales.head())
display(df_invoice.head())
display(df_product.head())


# ### Task 2: Basic Python and Pandas Operations
# #### Objective: Perform basic Python and Pandas operations to manipulate the data.
#
# <mark>Instructions:</mark>
#
# 1. Check for missing values in the Sales DataFrame.
#
# 2. Replace any NaN values in the Sales and UnitPrice columns with 0.
#
# 3. Calculate basic descriptive statistics for the Quantity and UnitPrice columns (mean, median, mode, standard deviation).

# In[2]:


# Code Task 2 here

# 1.Check for missing values using .isnull function
missing_values = df_sales.isnull()

# Display only rows with null values
rows_with_nulls = df_sales[missing_values.any(axis=1)]

# Display the rows with null values
display(rows_with_nulls)

# 2. Replace NaN values in Quantity and UnitPrice columns with 0
df_sales['Quantity'] = df_sales['Quantity'].fillna(0)
df_sales['UnitPrice'] = df_sales['UnitPrice'].fillna(0)

# 3.Descriptive statistics for the 'Quantity' and 'UnitPrice'.
# descriptive statistics for the Quantity Column
mean_quantity = df_sales['Quantity'].mean()
median_quantity = df_sales['Quantity'].median()
# Mode returns a Series, so we extract the first value using .iloc[0]
mode_quantity = df_sales['Quantity'].mode().iloc[0]
std_quantity = df_sales['Quantity'].std()

# descriptive statistics for the UnitPrice Column
mean_UnitPrice = df_sales['UnitPrice'].mean()
median_UnitPrice = df_sales['UnitPrice'].median()
# Mode returns a Series, so we extract the first value using .iloc[0]
mode_UnitPrice = df_sales['UnitPrice'].mode().iloc[0]
std_UnitPrice = df_sales['UnitPrice'].std()

# Display the results
print(
    f"Quantity - Mean: {mean_quantity}, Median: {median_quantity}, Mode: {mode_quantity}, Std Dev: {std_quantity}")
print(
    f"UnitPrice - Mean: {mean_UnitPrice}, Median: {median_UnitPrice}, Mode: {mode_UnitPrice}, Std Dev: {std_UnitPrice}")


# ## Explanation of Steps
# * **Null Check:** Filters rows containing missing values to verify data integrity. The check confirmed that the dataset contains zero missing (`NaN`) values.
# * **Data Imputation:** Applies a `.fillna(0)` assignment to the `Quantity` and `UnitPrice` columns as a defensive step to prevent calculation errors.
# * **Statistical Profiling:** Generates a structured summary comparing the averages, midpoints, common values, and spreads of both metrics.
#

# ### Task 3:Merging DataFrames
# #### Objective: Merge the Sales, Invoice, and Product tablesbased on common Keys to perform a comprehensive analysis
#
# Instructions:
# #
# 1. Merge the Sales DataFrame with the Invoice DataFrame on InvoiceNo.
# #
# 2. Merge the result with the Product DataFrame on StockCode

# In[3]:


# Code Task 3 here

# Merge the Sales and Invoice DataFrames on 'InvoiceNo'
df_combined = pd.merge(df_sales, df_invoice, on='InvoiceNo')
# Merge the result df_combined with the Product DataFrame df_product on StockCode
df_mergeresult = pd.merge(df_combined, df_product, on='StockCode')

# Display the first few rows of the merged DataFrame
display(df_mergeresult.head())


# ### Objective
# Combine the three separate relational DataFrames (`Sales`, `Invoice`, and `Product`) into a single unified dataset using common keys.
#
# ### Explanation of Steps
# * **Relational Joins:** Uses `pd.merge()` to link the tables sequentially based on shared relational keys.
# * **First Merge:** Connects `df_sales` and `df_invoice` using the unique identifier `InvoiceNo`.
# * **Second Merge:** Connects the combined result with `df_product` using `StockCode` to enrich the transactions with item descriptions.
#

# ## Task 4: Exploratory Data Analysis (EDA)
# ### Objective: Conduct EDA by analysing the data, identifying patterns, trends, and outliers.
#
# Instructions:
#
# Use describe() to calculate summary statistics for numeric columns.
#
# Perform basic filtering, such as filtering out sales with Quantity equal to 0.
#
# Check for outliers in the Sales column by using a scatter plot.

# In[4]:


# Code Task 4 here
# Importing seaborn matplotlib drivers
get_ipython().system('pip install seaborn matplotlib')


# ##### Environment and Library Setup
#
# ##### Objective
# Ensure that the necessary data visualization packages (`seaborn` and `matplotlib`) are installed and ready for use in the workspace environment.
#
# ##### Explanation of Steps
# * **Package Installation:** Uses the `!pip install` command to explicitly pull the latest compatible versions of the plotting libraries into the notebook session.
#

# In[5]:


# 1. calculate summary statistics for numeric columns such as 'Quantity' and 'UnitPrice' by using Use describe() function
df_sales[['Quantity', 'UnitPrice']].describe()


# ##### Objective
# Generate detailed summary statistics for numeric data columns to understand their distributions.
#
# ##### Explanation of Steps
# * **Statistical Profiling:** Uses the `.describe()` function to quickly calculate the count, mean, standard deviation, minimum, maximum, and percentiles for both `Quantity` and `UnitPrice`.
#

# In[6]:


# Importing matplotlib and seaborn libraries for visualization

# Filter out sales with Quantity equal to 0
df_filtered = df_mergeresult[df_mergeresult['Quantity'] != 0]
# Display the filtered DataFrame
display(df_filtered)


#  ##### Objective
# Filter the merged dataset to remove invalid transactions where the product quantity is zero.
#
# ##### Explanation of Steps
# * **Data Cleaning:** Filters `df_mergeresult` to exclude records where `Quantity` equals `0`, as these do not represent active retail sales.
# * **Result Verification:** Uses the `display()` function to inspect the clean, filtered dataset.
#

# In[7]:


# Check for outliers in the Sales column by using a scatter plot.

# Set the plotting style and figure size
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Create the scatter plot (Quantity is your actual sales volume data column)
sns.scatterplot(x=df_filtered.index,
                y=df_filtered['Quantity'], alpha=0.9, color='crimson')

# Add labels and titles updated to match the question wording
plt.title('Scatter Plot to Detect Outliers in Sales',
          fontsize=14, fontweight='bold')
plt.xlabel('Transaction Index', fontsize=12)
plt.ylabel('Sales (Quantity Sold)', fontsize=12)

# Display the plot
plt.show()


# ### Visual Analysis & Findings
# * **Outlier Identification:** The scatter plot reveals a critical anomaly near Transaction Index 40,000, where a single order exceeds 70,000 units.
# * **Data Distribution:** The vast majority of standard retail transactions remain tightly clustered near the baseline, comfortably below 5,000 units per order.
# * **Actionable Insight:** This extreme data point distorts the true average of the sales dataset. For accurate downstream analysis or modeling, this transaction should be isolated or removed using statistical filtering thresholds.
#

# 1. ## Task 5: Data Visualisation – Scatter Plot, Histogram, and Line Chart
# ### Objective: Create scatter plots, histograms, and line charts to better understand the data.
#
# Instructions:
#
# Use a scatter plot to examine the relationship between Quantity and Sales.
#
# Use a histogram to visualise the distribution of the Sales column.
#
# Use a line chart to show the trend of Sales over time.
#

# In[8]:


# Code Task 5 here

# 1. Calculate the Sales column (Quantity * Price)
df_filtered['Sales'] = df_filtered['Quantity'] * df_filtered['UnitPrice']

# 2. Set up the plotting canvas
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 3. Create a scatter plot comparing Quantity vs Sales
sns.scatterplot(data=df_filtered, x='Quantity',
                y='Sales', alpha=0.6, color='green')

# 4. Add clear titles and labels
plt.title('Relationship Between Quantity and Total Sales',
          fontsize=14, fontweight='bold')
plt.xlabel('Quantity Sold', fontsize=12)
plt.ylabel('Total Sales Value ($)', fontsize=12)

# 5. Display the plot
plt.show()


# ### Objective
# Examine the correlation between the volume of goods sold and the total financial revenue generated per transaction.
#
# ### Explanation of Steps
# * **Correlation Mapping:** Plots `Quantity Sold` against `Total Sales Value ($)` to visually evaluate how changes in transaction sizes scale revenue.
# * **Outlier Validation:** The visualization reveals that the high-volume transaction (~74,000 units) is also directly responsible for the highest revenue spike (~$77,000), confirming it is an extreme but consistent outlier across both metrics

# In[9]:


# Histogram to visualise the distribution of Sales
# 1. Set the canvas size
plt.figure(figsize=(8, 6))

# 2. Use a different variable name (sales_in_millions) so re-running won't break it
sales_in_millions = df_filtered['Sales'] / 1000000

# 3. Plot using df_filtered and the new un-squished values
sns.histplot(sales_in_millions, bins=5, color='purple', kde=True)

# 4. Add titles and clean labels
plt.title('Distribution of Sales', fontsize=14, fontweight='bold')
plt.xlabel('Sales (in Millions)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# 5. Display the perfect graph
plt.show()


# ### Objective
# Analyze the statistical spread and frequency of transaction values to evaluate overall data distribution skewness.
#
# ### Explanation of Steps
# * **Frequency Mapping:** Generates a histogram/distribution plot to evaluate the frequency profile of your sales revenue.
# * **Data Skew Analysis:** The visualization shows an extreme right-skewed pattern. Because one extreme outlier stretches the x-axis scale up to 0.08 million ($80,000), over 99% of normal retail transactions are heavily compressed into a single spike at the absolute baseline.
#

# In[10]:


# Line chart to visualise Profit over time

# 1. Group FIRST (This creates the monthly_sales DataFrame)
monthly_sales = df_filtered.groupby(df_filtered['InvoiceDate'].dt.to_period('M'))[
    'Sales'].sum().reset_index()

# 2. Format the labels SECOND (Now monthly_sales exists and can be modified)
monthly_sales['month_year'] = monthly_sales['InvoiceDate'].dt.strftime('%m-%Y')

# 3. Make the canvas wider
sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 6))

# 4. Create the line chart
sns.lineplot(data=monthly_sales, x='month_year', y='Sales',
             marker='o', color='teal', linewidth=2.5)

# 5. Add titles and labels
plt.title('Monthly Sales Trend Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Month-Year', fontsize=12)
plt.ylabel('Total Sales Value ($)', fontsize=12)

# 6. Change rotation to 90 degrees so labels never overlap
plt.xticks(rotation=90, fontsize=10)

# 7. Display the clean plot
plt.tight_layout()
plt.show()


# ### Objective
# Track performance changes and identify seasonal patterns over multiple years using a time-series line plot.
#
# ### Explanation of Steps
# * **Trend Tracking:** Maps monthly transaction aggregates chronologically to observe performance cycles across years.
# * **Peak Identification:** The line chart reveals a massive revenue peak in October 2016, along with recurring fluctuations across standard seasonal cycles.
#

# ## Task 6: Correlation and Data Insights
# ### Objective: Identify the relationship between different numerical columns in the dataset.
#
# Instructions:
#
# Calculate the correlation between Quantity and Sales.
#
# Visualise the correlation matrix using a heatmap.

# In[11]:


# Code Task 6 here

# Calculate correlation between 'UnitsSold' and 'Sales'
correlation = df_filtered[['Quantity', 'Sales']].corr()

# Display the correlation matrix
print(correlation)

# Create a heatmap for the correlation matrix
plt.figure(figsize=(6, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm',
            fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix between Quantity and Sales')
plt.show()


# ### Objective
# Measure the mathematical strength of the relationship between product quantities and total sales values using a correlation matrix heatmap.
#
# ### Explanation of Steps
# * **Matrix Heatmap:** Plots a correlation matrix using `sns.heatmap()` to evaluate numeric relationships visually.
# * **Strong Linear Correlation:** The matrix shows a nearly perfect positive correlation of `0.98` between `Quantity` and `Sales`, confirming that transaction volumes directly drive revenue levels.
#

# ## Task 7: Grouping and Aggregating
# ### Objective: Perform grouping and aggregation operations to summarise the data.
#
# Instructions:
#
# GroupBy operation: Group by Product_Category and calculate the total Sales per category.
#
# Create a Pivot Table to show Sales by Country and Product_Category.

# In[12]:


# Code Task 7 here

# Group by the detected product_category column and calculate total Sales
sales_by_category = df_filtered.groupby('Product_Category')[
    'Sales'].sum().reset_index()

# Sort categories from highest sales to lowest
sales_by_category = sales_by_category.sort_values(by='Sales', ascending=False)

# Display the grouped data
display(sales_by_category)


# In[13]:


# Create a pivot table for Sales by Country and ProductCategory
pivot_table = df_filtered.pivot_table(
    values='Sales', index='Country', columns='Product_Category', aggfunc='sum', fill_value=0)

# Reset the index to make 'Country' a normal column
pivot_table = pivot_table.reset_index()

# Display the pivot table
display(pivot_table)


# In[14]:


# Bar chart to show total Sales by Country
# Group data by Country, convert sales to Millions, and sort descending
sales_by_Country = df_filtered.groupby('Country')['Sales'].sum().reset_index()
sales_by_Country['Sales'] = sales_by_Country['Sales']/1000000
sales_by_Country = sales_by_Country.sort_values(by='Sales', ascending=False)
# Use Fabric's built-in interactive rendering to display the summary table
display(sales_by_Country)
# Configure plot window dimensions
plt.figure(figsize=(12, 6))
# Generate horizontal bar chart with corrected axis labels
sns.barplot(x='Sales', y='Country', data=sales_by_Country,
            color='green', orient='h')
plt.title('Sales by Country')
plt.xlabel('Country')
plt.ylabel('Total Sales in Millions')
plt.show()


# ##### Regional Sales Analysis Findings
#
# ### Key Insights
# * **Market Dominance:** The United Kingdom represents the overwhelming majority of total revenue, cross-cutting over 1.6 Million in scaled sales.
# * **Secondary Markets:** Germany and France lead the secondary tier of international markets, though they remain significantly smaller than the primary UK cluster.
# * **Long Tail Distribution:** The remaining global regions exhibit a steep drop-off, demonstrating a highly centralized geographic consumer base.
#

# In[15]:


# Bar chart to show total Sales by product_Catergory
sales_by_Product_Category = df_filtered.groupby(
    'Product_Category')['Sales'].sum().reset_index()
sales_by_Product_Category['Sales'] = sales_by_Product_Category['Sales']/1000000
sales_by_Product_Category = sales_by_Product_Category.sort_values(
    by='Sales', ascending=False)
display(sales_by_Product_Category)


# In[16]:


# 1. Set a much taller figure size so labels have room to breathe
plt.figure(figsize=(12, 10))

# 2. Slice the dataframe to take only the top 20 rows (.head(20))
top_categories = sales_by_Product_Category.head(20)

# 3. Create the barplot using the top 20 data
sns.barplot(x='Sales', y='Product_Category',
            data=top_categories, color='green', orient='h')

# 4. Corrected titles and axis labels
plt.title('Top 20 Sales by Product Category', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales in Millions', fontsize=12)
plt.ylabel('Product Category', fontsize=12)

# 5. Prevent text clipping
plt.tight_layout()
plt.show()


# ##### Product Category Sales Analysis Findings
#
# ###### Key Insights
# * **Dominant Segment:** The "Uncategorized" product segment holds the highest sales volume by a significant margin, suggesting a large portion of inventory lacks specific metadata classification.
# * **Seasonal and Decor Trends:** Among classified products, holiday items ("CHRISTMAS") and home accents ("CANDLE", "GLASS", "MUG") serve as primary revenue drivers.
# * **Inventory Focus:** The steep drop-off after the top categories highlights where the core retail demand concentrates, providing clear direction for stock management.
#

# ### Project Summary: Key Takeaways
# ######
# ###### 1. Data Quality
# * **Clean Data:** The sheets loaded perfectly and had zero missing values (`NaN`).
# * **Safe Coding:** We still cleaned the `Quantity` and `UnitPrice` columns as a defensive step to prevent future math errors.
# ######
# ###### 2. The Big Outlier
# * **One Huge Sale:** We found one massive order of **74,000+ items** (~$77,000 in revenue).
# * **Data Distortion:** This single customer order stretches the graphs and pulls the "average" sales number way too high. It acts as a wholesale business order rather than a normal retail shopper.
#
# ###### 3. Top Country
# * **UK Dominance:** The United Kingdom is the primary market by a massive margin, pulling in over **1.6 Million** in sales.
# * **Other Markets:** Germany and France lead the secondary markets, but they are much smaller than the UK.
#
# ###### 4. Top Products
# * **Missing Labels:** The number one sales category is **"Uncategorized"**, showing that the store needs to label its backend inventory system better.
# * **Popular Items:** Christmas items, candles, mugs, and glass decor are the top-selling actual products.
#

# ## Submission Guidelines:
# Submit the Python notebook with all the tasks and visualisations.
#
# Ensure that each task is clearly explained and that all steps are followed.
#
# Include markdown explanations where necessary to explain your thought process.

# Good work. Well done.

# In[ ]:
