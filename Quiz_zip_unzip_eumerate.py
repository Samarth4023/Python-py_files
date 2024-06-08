#!/usr/bin/env python
# coding: utf-8

# # 1) Zip Coordinates.

# In[37]:


# Given lists of coordinates and labels
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ['F', 'J', 'A', 'Q', 'Y', 'B', 'W', 'X']

# Create a list of formatted points combining labels and coordinates
points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {}, {}, {}'.format(*point))

# Print each point
for point in points:
    print(point)


# # 2) Zip lists to Dictionary.

# In[39]:


# List of cast member names
cast_names = ['Barney', 'Robin', 'Ted', 'Lilly', 'Marshall']

# List of cast member heights in inches
cast_heights = [72, 68, 72, 66, 76]

# Create a dictionary by zipping cast names with their corresponding heights
cast = dict(zip(cast_names, cast_heights))

# Print the resulting dictionary
print(cast)


# # 3) Unzip Tuples.

# In[35]:


# Tuple containing cast members' names and their corresponding heights
cast = (('Barney', 72), ('Robin', 68), ('Ted', 72), ('Lilly', 66), ('Marshall', 76))

# Unzip the cast tuple into two separate tuples: names and heights
names, heights = zip(*cast)

# Print the tuple containing the names
print(names)

# Print the tuple containing the heights
print(heights)


# # 4) Transpose with Zip.

# In[33]:


# Tuple containing tuples of sequential numbers
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

# Transpose the data tuple, swapping rows with columns
data_transpose = tuple(zip(*data))

# Print the transposed tuple
print(data_transpose)


# # 5) Enumerate.

# In[41]:


# List of cast member names
cast = ['Barney Stinson', 'Robin Scherbatsky', 'Ted Mosby', 'Lilly Aldrin', 'Marshall Ericksen']

# List of cast member heights in inches
heights = [72, 68, 72, 66, 76]

# Loop through each character in the cast list by index and name
for i, character in enumerate(cast):
    # Append the corresponding height to the character's name
    cast[i] = character + " " + str(heights[i])

# Print the updated cast list with heights included
print(cast)

