#!/usr/bin/env python
# coding: utf-8

# # Only Keys

# In[18]:


# Create a dictionary called book_title with word frequencies
book_title = {'great': 1, 'expectaions': 2, 'the': 3, 'of': 4, 'the': 5}

# Iterate through each key (word) in the book_title dictionary
for key in book_title:
    # Print the key (word)
    print(key)


# # Both Keys & Values

# In[23]:


# Create a dictionary called book_title with word frequencies
book_title = {'great': 1, 'expectaions': 2, 'the': 3, 'of': 4, 'the': 5}

# Iterate through each key-value pair in the book_title dictionary
for key, value in book_title.items():
    # Print the key (word) and its corresponding value (frequency)
    print('Key: {}, Value: {}'.format(key, value))


# # Example

# ## count total fruits

# In[28]:


# Initialize a variable to store the total count
result = 0

# A dictionary representing items in a basket and their quantities
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

# A list of fruits we want to consider
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through each key-value pair in the basket_items dictionary
for fruit, count in basket_items.items():
    # Check if the fruit is in the list of desired fruits
    if fruit in fruits:
        # Add the quantity of the fruit to the result
        result += count

# Print the total count of desired fruits
print(result)


# ## count fruits and not fruits

# In[34]:


# Initialize a variable to store the total count
fruit_count, not_fruit_count = 0, 0

# A dictionary representing items in a basket and their quantities
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

# A list of fruits we want to consider
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through each key-value pair in the basket_items dictionary
for fruit, count in basket_items.items():
    # Check if the fruit is in the list of desired fruits
    if fruit in fruits:
        # Add the quantity of the fruit to the result
        fruit_count += 1
    else:
        # Add the quantity of the not_fruit to the result
        not_fruit_count += 1
        
# Print the total count of types of fruits
print(fruit_count)
# Print the total count of not_fruits
print(not_fruit_count)

