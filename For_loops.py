#!/usr/bin/env python
# coding: utf-8

# # For Loops

# ## Iterable: An object that can return one of its elements at a time.

# In[22]:


# Create a list of months
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

# Iterate through each month and print its title (capitalized)
for month in months:
    print(month.title())            # Convert the month name to title case


# In[24]:


# Create a list of cities
cities = ['pune', 'mumbai', 'new york', 'jakarta']
# Initialize an empty list to store capitalized city names
capitalize_cities = []
# Iterate through each city in the list
for city in cities:
    # Capitalize the first letter of each city name and add it to the new list
    capitalize_cities.append(city.title())
# Print the list of capitalized city names
print(capitalize_cities)

