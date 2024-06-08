#!/usr/bin/env python
# coding: utf-8

# # Dictionaries

# ### A Datatype for mutable objects that stores mapping of unique keys to values
# ### Stores pairs of elements, keys and values and it is uordered.

# In[11]:


elements = {'hydogen': 1, 'helium': 2, 'carbon':6}
# hydrogen, helium, carbon ----> keys  && 1,2,6 ----> assigned values
print(elements['carbon'])
#we can lookup values by using[] enclosing key


# ## adding elements to dictionary

# In[6]:


elements = {'hydogen': 1, 'helium': 2, 'carbon':6}
elements ['lithium'] = 3
print(elements)


# ## get()

# In[14]:


elements = {'hydogen': 1, 'helium': 2, 'carbon':6, 'lithium':3}
print(elements.get('dilithium'))


# In[16]:


elements = {'hydogen': 1, 'helium': 2, 'carbon':6, 'lithium':3}
print(elements.get('helium'))


# ## is & is not operator

# In[25]:


# is operator

elements = {'hydogen': 1, 'helium': 2, 'carbon':6, 'lithium':3}
x = elements.get('dilithium')
is_null = x is None
print(is_null)


# In[27]:


# is not operator

elements = {'hydogen': 1, 'helium': 2, 'carbon':6, 'lithium':3}
x = elements.get('dilithium')
is_null = x is not None
print(is_null)


# #### Note: If you define a variable with an empty set of curly braces like this: a={}, Python will assign an empty dictionary to that variable.You can always use set() & dict() to define empty sets and dictionaries as well. 

# ## Compound Data Stuctures

# In[41]:


elements = {'hydrogen':{'number':1, 'weight':1.00794, 'symbol':'H'}, 'helium':{'number':2, 'weight':4.002602, 'symbol': 'He'}}
print(elements['helium'])
print(elements['helium']['weight'])
print(elements.get('unobotium','There\'s no such element'))

