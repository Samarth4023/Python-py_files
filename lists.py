#!/usr/bin/env python
# coding: utf-8

# In[10]:


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(months[1])
print(months[0])
print(months[10])
print(months[-1])
print(months[-5])


# ## Slicing

# In[16]:


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(months[6:9])
# lower index is inclusive
# upper index is exclusive


# In[14]:


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(months[:6])


# In[12]:


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(months[6:])


# In[20]:


string = "Hello World!"
print(string[6:9])


# In[22]:


string = "Hello World!"
print(string[6:])


# In[24]:


string = "Hello World!"
print(string[:9])


# ## List Modifications

# In[4]:


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
months[3] = 'Friday'
months[5] = 7
print(months)

