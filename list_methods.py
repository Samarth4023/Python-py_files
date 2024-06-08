#!/usr/bin/env python
# coding: utf-8

# ## len()

# In[15]:


# prints the total number of elements present in the list

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(len(months))


# ## max()

# In[19]:


# returns the greatest element of a list

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(max(months))
# in strings, the element that would occur last if the list was sorted alphabetically

numbers = [23, 34, 12, 45, 89, 1, 8, 99]
print(max(numbers))
# prints the largest number if integers


# ## min()

# In[24]:


# returns the samllest element of a list

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(min(months))
# in strings, the element that would occur first if the list was sorted alphabetically

numbers = [23, 34, 12, 45, 89, 1, 8, 99]
print(min(numbers))
# prints the smallest number if integers


# ## sorted()

# In[28]:


# returns a copy of the list in order form samllest to largest leaving the original list unchanged.

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(sorted(months))
# sorts in alphabetical order

numbers = [23, 34, 12, 45, 89, 1, 8, 99]
print(sorted(numbers))
# sorts based on integers


# ## reverse sorting.

# In[39]:


# returns a copy of the list in order form largest to smallest leaving the original list unchanged.

#--------------------------------TRUE--------------------------------
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(sorted(months, reverse = True))

numbers = [23, 34, 12, 45, 89, 1, 8, 99]
print(sorted(numbers, reverse = True))

#--------------------------------FALSE--------------------------------

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(sorted(months, reverse = False))

numbers = [23, 34, 12, 45, 89, 1, 8, 99]
print(sorted(numbers, reverse = False))


# In[ ]:




