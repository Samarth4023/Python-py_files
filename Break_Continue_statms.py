#!/usr/bin/env python
# coding: utf-8

# # Break
# ## Terminates a for or while loop.

# In[22]:


# Given list of cargo items and their weights
manifest = [('bananas', 15), ('matt', 34), ('dog kennels', 42), ('machine', 120), ('chesses', 5)]

# Initialize variables
weight = 0
items = []

# Iterate through each cargo in the manifest
for cargo in manifest:
    # Check if the total weight exceeds 100
    if weight > 100:
        break
    else:
        # Add the name of the cargo item to the list
        items.append(cargo[0])
        # Update the total weight
        weight += cargo[1]

# Print the final total weight and the list of items
print("Total weight:", weight)
print("Items in the manifest:", items)


# # Continue
# ## Terminates one iteration of a for or while loop.

# In[24]:


# Given lists of fruits and foods
fruit = ['orange', 'strawberry', 'apple']
foods = ['apple', 'strawberry', 'hummus', 'toast']

# Initialize a counter for fruits
fruit_count = 0

# Iterate through each food item
for food in foods:
    # Check if the food is not in the fruit list
    if food not in fruit:
        print('Not a Fruit!')  # Print a message
        continue  # Skip to the next iteration
    else:
        # If it's a fruit, increment the fruit count
        fruit_count += 1
        print('Found a Fruit!')  # Print a message

# Print the total number of fruits found
print('Total Fruits:', fruit_count)

