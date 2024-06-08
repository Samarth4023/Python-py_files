#!/usr/bin/env python
# coding: utf-8

# # Truth Value Testing

# #### If we use non-boolean object as a condition in an if statement in place of the boolean expression, Python will check for its truth value and use that to decide whether or not to run the indented code. By default, the truth value of a object in python is considered true unless specified false in the documentation

# ### Here are the most of the built-in objects that are considered false in python.
# ### --constants defined to be false: None and False
# ### --zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction (0, 1)
# ### --empty sequences and collections: " ", (), [], {}, set(), range(0)

# In[7]:


points = 174
prize = None        # default to none

# use the value of points to assign prize
if points <=50:
    prize = "Wooden Rabbit"
elif 151 <= points <= 180:
    prize = "Wafer-thin mint"
elif points >=181:
    prize = "Penguin"

#use the value of points to assign result
if prize:
    result = 'Congratulations! You won a {}'.format(prize)
else:
    result = 'Oh Dear ! No prize this time.'

print(result)

