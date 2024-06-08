#!/usr/bin/env python
# coding: utf-8

# # Functions

# ## - Functions are useful chunks of code that allow us to encapsulate a task.
# ## * Encapsulation is a way to carry out a whole series of steps with one simple command.
# ## - Functions are also used in to help organzie and optimize code.

# In[5]:


# Defining Functions
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2
cylinder_volume(10, 3)


# ## with no arguments

# In[10]:


def print_greeting():
    print('Hello World!')              # no return but still a valid function


# ## Local Variable

# ### - It can be only used within the body of a function

# In[ ]:





# ## Return Keyword

# ### Used to give back an output value when the function is called
# ### - If there is no return statement, the function returns None.
# ### - The value of the expresssion that follows return is the output of the function.

# In[ ]:


volume = height * pi * radius ** 2
return volume


# ## Print as a function

# ### - Print provides output to the console while return provides the value that you can store and work with and code later.

# In[ ]:





# ## Variable Scope

# ### - The parts of a program that a variable can be referenced, or used, from.

# In[ ]:





# ## Docstring (Documentation String)
# ### - A type of comment used to explain the purpose of a function and how  it should be used.

# In[ ]:




