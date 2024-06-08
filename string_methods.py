#!/usr/bin/env python
# coding: utf-8

# ## join()

# In[9]:


# it takes a list as an argument and returns a string consisting of the list elements joined by seperator string.

nautical_directions = "\n".join(['fore', 'aft', 'starboard', 'port'])
print(nautical_directions)


# ## append()

# In[11]:


# adds an element to the end of the lists.

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
months.append("Dec")
print(months)

