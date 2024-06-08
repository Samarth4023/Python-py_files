#!/usr/bin/env python
# coding: utf-8

# # Zip

# ### Returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables.

# In[15]:


# Given lists of items and their corresponding weights
items = ['bananas', 'matt', 'dog kennels', 'machine', 'chesses']
weights = [15, 34, 42, 120, 5]

# Use the zip function to pair items with their weights
# The resulting list contains tuples where each tuple has an item and its weight
print(list(zip(items, weights)))
print('\n')

#--------------OR------------------

# The resulting iterator produces tuples where each tuple has an item and its weight
for cargo in zip(items, weights):
    print(cargo[0], cargo[1])
print('\n')

#--------------OR------------------

# The resulting iterator produces tuples where each tuple has an item and its weight
for item, weight in zip(items, weights):
    print(item, weight)


# # Unzip

# In[30]:


# Given a list of cargo items and their corresponding weights
manifest = [('bananas', 15), ('matt', 34), ('dog kennels', 42), ('machine', 120), ('chesses', 5)]

# Unzip the manifest into separate lists for items and weights
items, weights = zip(*manifest)

# Print the items and weights
print("Items:", items)
print("Weights:", weights)


# # Eumerate

# ### Enumerate is a special built-in function, it returns these tuples containing the indices and values of a list, in an iterable for you.

# In[32]:


# Given list of items
items = ['bananas', 'matt', 'dog kennels', 'machine', 'chesses']

# Using zip and range to iterate through items with their indices
for i, item in zip(range(len(items)), items):
    print(i, item)  # Print the index and the item name

print('\n')  # Add a newline for clarity

# Using enumerate to directly iterate through items with their indices
for i, item in enumerate(items):
    print(i, item)  # Print the index and the item name

