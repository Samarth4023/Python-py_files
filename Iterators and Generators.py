#!/usr/bin/env python
# coding: utf-8

# # Iterators
# ### An Iterator is an object that represents a stream of data.

# # Generators
# ### Generators are a simple way to create iterators using functions.

# # Generator Function

# In[1]:


# Define a custom generator function called "my_range"
def my_range(x):
    i = 0
    while i < x:
        yield i  # Yield the current value of 'i'
        i += 1   # Increment 'i' by 1

# Call the generator function with an argument of 4
# This will create an iterator that generates values from 0 to 3
print(my_range(4))


# In[5]:


# Define a custom generator function called "my_range"
def my_range(x):
    i = 0
    while i < x:
        yield i  # Yield the current value of 'i'
        i += 1   # Increment 'i' by 1

# Call the generator function with an argument of 5
# This will create an iterator that generates values from 0 to 4
for x in my_range(5):
    print(x)


# In[7]:


# Given a list of lessons
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

# Define a custom generator function called "my_enumerate"
def my_enumerate(iterable, start=0):
    # Initialize a counter
    count = start
    # Iterate through the elements in the iterable
    for element in iterable:
        # Yield the current count and the element
        yield count, element
        # Increment the count by 1
        count += 1

# Use the custom generator function to enumerate the lessons
for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


# # Practice Quiz: Chunker

# In[9]:


# Define a generator function called "chunker"
def chunker(iterable, size):
    # Iterate through the iterable in chunks of the specified size
    for i in range(0, len(iterable), size):
        # Yield a slice of the iterable from index 'i' to 'i + size'
        yield iterable[i:i + size]

# Use the chunker generator function to split the range(25) into chunks of size 4
for chunk in chunker(range(25), 4):
    # Print each chunk as a list
    print(list(chunk))


# # Why Generators ?
# ### Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.

# # Generator Expressions
# ### Cool concept of that combines generators and list comprehensions!
# ### You can actually create a generator in the same way you'd normally write a list comprehension, except with parenthesis instead of square brackets.

# In[7]:


sq_list = [x ** 2 for x in range(10)]
# this produces a list of squares
print(sq_list)


# In[11]:


sq_iterator = (x ** 2 for x in range(10))
# this produces an iterator of squares
print(sq_iterator)

