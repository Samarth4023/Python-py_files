#!/usr/bin/env python
# coding: utf-8

# # Lambda Expressions
# ### - Expression used to create on anonymous function (i.e., functions that don't have a name)

# ## Example
# ### - Regular Function

# In[14]:


def double(x):
    return x * 2


# ### - Equivalent Lambda Expression

# In[28]:


double = lambda num: num * 2
double = lambda x: x * 2      # lambda ----> keyword     
# x ----> following lambda or one or more arguments for the anonymous function and then a colon

double(3)

# lambda x, y: x * y (remove comment for test purposes)


# # Lambda with Map
# ### - map() is a higher-order built-in function that makes a function and iterable as inputs and returns an iterator that applies the function to each element of the iterable.

# In[36]:


# Given a list of lists containing numbers
numbers = [
    [34, 63, 88, 71, 29],
    [90, 78, 51, 27, 45],
    [63, 37, 85, 46, 22],
    [51, 22, 34, 11, 18]
]

# Use the map() function with a lambda expression to calculate the average for each sublist
averages = list(map(lambda x: sum(x) / len(x), numbers))

# Print the resulting list of averages
print(averages)


# # Lambda with Filter
# ### - filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an itertor with the elements from the iterable for which the function returns True.

# In[34]:


# Given a list of cities
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

# Use the filter() function with a lambda expression to filter cities with names shorter than 10 characters
short_cities = list(filter(lambda x: len(x) < 10, cities))

# Print the resulting list of short cities
print(short_cities)

