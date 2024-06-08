#!/usr/bin/env python
# coding: utf-8

# # Quiz 1

# In[8]:


# Create a list of full names
names = ['Joey Tribbiani', 'Monica Gellar', 'Chandler Bing', 'Phueobe Buffay']
# Initialize an empty list to store usernames
usernames = []

# Iterate through each full name
for u_names in names:
    # Convert the name to lowercase and replace spaces with underscores
    usernames.append(u_names.casefold().replace(" ", "_"))
# Print the list of generated usernames
print(usernames)


# In[10]:


# Create a list of full names
names = ['Joey Tribbiani', 'Monica Gellar', 'Chandler Bing', 'Phueobe Buffay']
# Iterate through each full name
for u_names in names:
    # Convert and print the name to lowercase and replace spaces with underscores
    print(u_names.casefold().replace(" ", "_"))


# # Quiz 2

# In[14]:


items = ['first string', 'second string']
html_str = "</u>\n"

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"
print(html_str)


# In[ ]:




