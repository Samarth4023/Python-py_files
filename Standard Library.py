#!/usr/bin/env python
# coding: utf-8

# # Standard Library

# ## Compute an Exponent

# In[1]:


import math
print(math.e**3)
print(math.exp(3))# print e to the power of 3 using the math module


# ## Password Generator

# In[2]:


# TODO: First import the `random` module
import random

# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# TODO: Add your function generate_password below
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
	return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
# Now we test the function
print(generate_password())

