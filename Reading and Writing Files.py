#!/usr/bin/env python
# coding: utf-8

# # Read a file

# In[49]:


# Open the file "hello.txt" in read mode
f = open("hello.txt", "r")

# Read the contents of the file
file_data = f.read()

# Close the file to free up system resources
f.close()

# Print the contents of the file
print(file_data)


# # too many files open

# In[57]:


# Initialize an empty list to store file objects
files = []

# Loop 10,000 times
for i in range(10000):
    # Open the file "hello.txt" in read mode and append the file object to the list
    files.append(open("hello.txt", "r"))

    # Print the current iteration number
    print(i)


# # Creating new file thru Python Code

# In[53]:


# Open the file "another_file.txt" in write mode
f = open("another_file.txt", "w")

# Write the string 'Hello World!' to the file
f.write('Hello World!')

# Close the file to save the changes
f.close()


# # auto close the file without using f.close()

# In[55]:


# Open the file "another_file.txt" in read mode using a context manager
with open("another_file.txt", "r") as f:
    # Read the contents of the file
    file_data = f.read()

# Print the contents of the file
print(file_data)

