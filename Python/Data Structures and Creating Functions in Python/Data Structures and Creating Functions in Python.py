#!/usr/bin/env python
# coding: utf-8

# ## Data Structures and Creating Functions in Python
#
# New notebook

# ## Data Structures and Creating Functions in Python
#
# **Exercise 1**
# Create a tuple that contains three numbers and print the last number from the tuple.
#
# **Exercise 2:**
# Create two sets and perform a union and an intersection operation between them.
#
# **Exercise 3:**
# Create a dictionary for a book with keys title, author, and year, and print the value for the author key.
#
# **Exercise 4**
# Create a list of your three favorite fruits and print the second fruit from the list.
#
# **Exercise 5: Control Structures**
# Write a program that asks for your age and prints whether you are eligible to vote (18 or older).
#
# **Exercise 6: Functions**
# Create a function that takes two numbers and returns their difference. Call the function with different numbers and print the result.

# In[ ]:


Joses_Book = {"Book_Name": "Counting Miracles",
              "Author": "Nicolas Spark", "Year": 2025}
print(Joses_Book["Book_Name"])


# In[ ]:


# Code Here Exercise 1

my_tuple = (9, 8, 8.99)

print(my_tuple[-1])  # Output:8.99


# In[ ]:


# Code Here Exercise 2
set1 = {6, 7, 8, 9}
set2 = {9, 10, 11, 12}
# Set union
print(set1 | set2)  # Output: {6,7,8,9,10,11,12}

# Set Intersection
print(set1 & set2)  # Output: {9}


# In[ ]:


# Code Here Exercise 3
# Creating a dictionary
book_info = {
    "title": "Counting Miracles",
    "author": "Nicholas Spark",
    "year": 2025,
}

# Print the value for the author key
print(book_info["author"])


# In[ ]:


# Code Here Exercise 4
my_fav_fruits = ["grape", "Mango", "Bananas"]

print(my_fav_fruits[1])


# In[ ]:


# Code Here Exercise 5
age = 16  # Ask the user for their age and convert it to an integer
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to voter.")


# In[ ]:


#  Code Here Exercise 6
# Function that takes two numbers and returns their difference
def find_difference(a, b):
    return a - b


# Test Call 1: Positive results
result_1 = find_difference(10, 5)
print(f"The difference between 15 and 5 is: {result_1}")

# Test Call 2: Resulting in a negative number
result_2 = find_difference(5, 25)
print(f"The difference between 10 and 25 is: {result_2}")

# Test Call 3: Using decimal numbers (floats)
result_3 = find_difference(6.5, 3.2)
print(f"The difference between 8.5 and 3.2 is: {result_3}")


# In[ ]:
