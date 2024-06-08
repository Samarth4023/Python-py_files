#!/usr/bin/env python
# coding: utf-8

# # Ranges

# In[23]:


# Create a list of integers using the range function
# The range function generates numbers from 0 (inclusive) up to 4 (exclusive)
print(list(range(4)))


# In[21]:


# Create a list of integers using the range function
# The range function generates numbers from 2 (inclusive) up to 6 (exclusive)
print(list(range(2, 6)))


# In[25]:


# Create a list of odd numbers using the range function
# The range function starts from 1 (inclusive), goes up to 20 (exclusive), and increments by 2
print(list(range(1, 20, 2)))


# # Ranges in for loop

# In[27]:


# Create a list of cities
cities = ['pune', 'mumbai', 'new york', 'jakarta']
# Iterate through each city using its index
for index in range (len(cities)):
    # Capitalize the first letter of each city name
    cities[index] = cities[index].title()
# Print the updated list of cities
print(cities)


# In[29]:


# Iterate through the range from 0 to 2 (3 times)
for i in range(3):
    # Print 'Hello!' for each iteration
    print('Hello!')

