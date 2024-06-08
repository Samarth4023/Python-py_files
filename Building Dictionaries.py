#!/usr/bin/env python
# coding: utf-8

# ## 1) Using a for loop to create a set of counters.

# ### Keeping track of the total count of each word.

# In[14]:


# Create a list of book titles
book_title = ['great', 'expectaions', 'the', 'of', 'the']

# Initialize an empty dictionary to count word occurrences
word_counter = {}

# Iterate through each word in the book_title list
for word in book_title:
    # If the word is not already a key in word_counter, add it with an initial count of 1
    if word not in word_counter:
        word_counter[word] = 1
    else:
        # If the word is already a key, increment its count by 1
        word_counter[word] += 1

# Print the word_counter dictionary
print(word_counter)


# ## 2) Using get method

# ### Keeping track of the total count of each word.

# In[16]:


# Create a list of book titles
book_title = ['great', 'expectaions', 'the', 'of', 'the']

# Initialize an empty dictionary to count word occurrences
word_counter = {}

# Iterate through each word in the book_title list
for word in book_title:
    # Use the get() method to retrieve the current count for the word
    # If the word is not already a key in word_counter, default to 0
    word_counter[word] = word_counter.get(word, 0) + 1

# Print the word_counter dictionary
print(word_counter)

