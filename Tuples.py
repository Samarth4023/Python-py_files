#!/usr/bin/env python
# coding: utf-8

# # Tuples
# ## A datatype for immutable ordered sequences of elements.
# ### Tuples cannot be added or remove items or sort them in place.

# In[5]:


# Tuples are used to store related pieces of information
dimensions = 52, 40, 100
length, width, height = dimensions
# tuple unpacking
print('The dimensions are {} * {} * {}'.format(length, width, height))


# ### You can also use tuple unpacking for assigning the information from a tuple into multiple variables without having to access them one by one, and make multiple assignment statements.
