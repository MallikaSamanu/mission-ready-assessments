#!/usr/bin/env python
# coding: utf-8

# ## Exploring and Analyzing Data with Pandas
#
# New notebook

# ## Exploring and Analyzing Data with Pandas
#
# Objective:
#
# In this mission, you will perform Exploratory Data Analysis (EDA) and basic data manipulation using Pandas. You will work with a dataset that includes information about employees and apply various data transformation techniques, including handling missing values, filtering, and performing basic data analysis.
#
# Dataset Overview:
#
# The dataset contains the following columns:
#
# employee_id: Unique identifier for each employee.
#
# name: Name of the employee.
#
# age: Age of the employee.
#
# department: The department where the employee works (e.g., HR, Engineering, Marketing).
#
# salary: Annual salary of the employee.
#
# work_experience: Number of years of work experience the employee has.
#
#

# ## Task 1: Load the Data
# Objective: Load the dataset into a Pandas DataFrame.
#
# Instructions:
#
# Create a DataFrame from the provided dataset.
#
# Display the first few rows of the dataset to ensure it loaded correctly.

# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a basic dataset
data = {
    'employee_id': range(1, 21),
    'name': ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack', 'Karen', 'Leo', 'Mia', 'Nina', 'Olivia', 'Paul', 'Quinn', 'Rita'],
    'age': [22, 25, 28, 35, 40, 42, 50, 60, 65, 30, 28, 24, 37, 41, 48, 33, 29, 32, 45, 38],
    'department': ['HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales', 'HR', 'Engineering', 'Marketing', 'Finance', 'Sales'],
    'salary': [50000, 60000, 55000, 75000, 80000, 85000, 100000, 110000, 120000, 65000, 67000, 72000, 85000, 90000, 95000, 48000, 67000, 70000, 80000, 88000],
    'work_experience': [1, 3, 5, 7, 10, 12, 15, 18, 20, 3, 1, 6, 4, 8, 5, 7, 3, 2, 6, 5],
}


# ### Task 2: Data Exploration
#
# Objective: Explore the dataset to get an understanding of its structure.
#
# Instructions:
#
# Check for missing values in the dataset.
#
# Get the summary statistics of numeric columns (age, salary, work_experience).

# In[20]:


# ==========================================
# Instruction 1: Check for missing values
# ==========================================
df = pd.DataFrame(data)
# display(df)
# checking missing data in data set
# missing_data=df.isna()
# display(missing_data)
# checking missing data by column
missing_data = df.isna().sum()
print(missing_data)
# checking missing data percentage
# missing_data=df.isna().mean()*100
# display(missing_data)


# In[22]:


# ====================================================================================================
# Instruction 2 : Calculate mean, median, mode, and standard deviation for age, salary, work_experience
# ====================================================================================================

# Mean: The average value
mean_age = df['age'].mean()  # This gives the average of the 'age' column
median_age = df['age'].median()  # The middle value when data is sorted
mode_age = df['age'].mode()[0]  # The most frequent value in the 'age' column
# Standard deviation, which measures how spread out the values are
std_age = df['age'].std()

# For salary, we calculate the same statistics
mean_salary = df['salary'].mean()
median_salary = df['salary'].median()
mode_salary = df['salary'].mode()[0]
std_salary = df['salary'].std()
# work_experience, we calculate the same statistics
mean_work_experience = df['work_experience'].mean()
median_work_experience = df['work_experience'].median()
mode_work_experience = df['work_experience'].mode()[0]
std_work_experience = df['work_experience'].std()
print(
    f"age - Average age: {mean_age:.2f}, Median Sales: {median_age:.2f}, Mode: {mode_age:.2f}, Std Dev: {std_age:.2f}")
print(
    f"salary - Mean: {mean_salary:.2f}, Median: {median_salary:.2f}, Mode: {mode_salary:.2f}, Std Dev: {std_salary:.2f}")
print(f"work_experience - Mean: {mean_work_experience:.2f}, Median: {median_work_experience:.2f}, Mode: {mode_work_experience:.2f}, Std Dev: {std_work_experience:.2f}")


# ### Task 3: Data Transformation
#
# Objective: Perform basic data transformations such as creating new columns and renaming existing ones.
#
# Instructions:
#
# Create a new column called years_to_retirement by subtracting the age from 65.
#
# Rename the salary column to annual_salary.
#
# Sort the DataFrame based on work_experience in descending order.

# In[23]:


# ===================================================================================================
# Instructions 1:# Create a new column called years_to_retirement by subtracting the age from 65.
# ====================================================================================================
# Create the years_to_retirement column
df['years_to_retirement'] = 65 - df['age']
# Verify the new column was added correctly
print(df[['age', 'years_to_retirement']].head(10))


# =========================================================
# Instructions2: Rename the salary column to annual_salary.
# =========================================================
# Renaming the 'Sales' column to 'TotalSales'
df.rename(columns={'salary': 'annual_salary'}, inplace=True)
display(df)

# ===============================================================================
# Instructions3: Sort the DataFrame based on work_experience in descending order.
# ===============================================================================

# Sorting by 'Work_experience' in descending order
sorted_df = df.sort_values(by='work_experience', ascending=False)
display(sorted_df)


# ### Task 4: Handling Missing Data
#
# Objective: Handle missing data (if any).
#
# Instructions:
#
# Introduce some missing values in the annual_salary column.
#
# Handle the missing data by either filling it with the mean salary or dropping the rows with missing values.

#

# In[24]:


# =====================================================================
# Instructions1:Introduce some missing values in the annual_salary column.
# =====================================================================

# Introduce missing values by randomly removing 20% of the data
df['annual_salary'] = df['annual_salary'].sample(frac=0.8).reindex(df.index)

# Display the first 10 rows to verify the NaN values appeared
print(df[['age', 'annual_salary']].head(10))


# In[25]:


# ================================================================================
# Instructions2:Handle the missing data by either filling it with the mean salary
# ================================================================================
# Calculate the mean of the annual_salary column
mean_salary = df['annual_salary'].mean()

# Fill the missing NaN values with that mean and save it permanently
df['annual_salary'] = df['annual_salary'].fillna(mean_salary)

# Verify that there are zero missing values left in the column
print("Missing values remaining:", df['annual_salary'].isna().sum())


# ## Task 5: Data Filtering and Selection
# Objective: Select specific data based on conditions.
#
# Instructions:
#
# Filter the data to show only employees who are older than 30.
#
# Select only the columns name, age, and annual_salary.

# In[27]:


# ==========================================================================
# Instruction1: Filter the data to show only employees who are older than 30
# =========================================================================

filtered_df = df[df['age'] > 30]
display(filtered_df)

# ==========================================================================
# Instruction1: Select only the columns name, age, and annual_salary
# ===========================================================================
selected_column_df = df[['name', 'age', 'annual_salary']]
display(selected_column_df)


# ### Task 6: Data Aggregation
# Objective: Perform group-based aggregation.
#
# Instructions:
#
# Group the data by department and calculate the average salary for each department.

# In[41]:


# Grouping the data by department and calculate the average salary for each department.
salary_by_dept = df.groupby('department')['annual_salary'].mean().reset_index()
display(salary_by_dept)
salary_summary_by_dept = df.groupby(
    'department')['annual_salary'].describe().reset_index()
display(salary_summary_by_dept)


# In[ ]:
