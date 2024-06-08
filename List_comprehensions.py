#!/usr/bin/env python
# coding: utf-8

# # List Comprehensions

# In[6]:


# Given a list of cities
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

# Create a new list with capitalized versions of the city names
capitalized_cities = [city.title() for city in cities]

# Print the capitalized city names
print(capitalized_cities)


# ## Example with conditions also.

# In[20]:


# Not List Comprehension
squares = []
for x in range(9):
    squares.append(x**2)
print(squares)

# List Comprehension
squares = [x**2 for x in range(9)]
print(squares)

# squares of only even numbers.
squares = [x**2 for x in range(9) if x%2==0]
print(squares)

# another one :)
squares = [x**2 if x%2==0 else x + 3 for x in range(9) ]
print(squares)


# ### List Comprehensions are very cool tool provided from python because we can create lists really quickly and concisely.

# ## 1) Extract First Name

# In[14]:


# Given a list of full names
names = ['Rick Sanchez', 'Morthy Smith', 'Summer Smith', 'Jerry Smith', 'Beth Smith']

# Extract the first names (lowercased) from the full names
first_names = [name.split()[0].lower() for name in names]

# Print the resulting list of first names
print(first_names)


# ## 2) Multiples of Three (3)

# In[16]:


# Create a list of multiples of 3
multiplier_3 = [x * 3 for x in range(1, 21)]

# Print the resulting list
print(multiplier_3)


# ## 3) Filter names by zero

# In[18]:


# Given a dictionary of student scores
scores = {'Rick Sanchez': 70, 'Morthy Smith': 35, 'Summer Smith': 82, 'Jerry Smith': 23, 'Beth Smith': 98}

# Create a list of names for students who passed (score >= 65)
passed = [name for name, score in scores.items() if score >= 65]

# Print the list of passed students
print(passed)

