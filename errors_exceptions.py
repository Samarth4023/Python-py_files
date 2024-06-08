#!/usr/bin/env python
# coding: utf-8

# # Syntax Errors
# ### It occurs when python can't interpret our code, since we didn't follow the current syntax for python. These are errors you're likely to get when you make a typo, or you're first starting to learn Python.

# # Exceptions
# ### It occurs when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions in python, and you can see which exception is thrown in the error message.

# # ValueError Exception
# ### It occurs when a built-in operation or function is given in argument with the correct type but an inappropriate value.

# In[1]:


x = int(input("Enter a Number: "))
x += 20
print(x)


# # NameError Exception
# ### It occurs when it can't find the value for this variable when it tries to run it.

# In[3]:


print(nonexistent_variable)


# # Assertion Error
# ### An assert statement fails.

# In[2]:


# AssertionError with error_message.
x = 1
y = 0
assert y != 0, "Invalid Operation" # denominator can't be 0
print(x / y)


# # Index Error
# ### A sequence subscript is out of range.

# In[4]:


j = [1, 2, 4]
print(j[4])


# # Key Error
# ### A key can't be found in a dictionary.

# In[6]:


# Creating a Dictionary 
subjects = {'Sree': 'Maths', 
			'Ram': 'Biology', 
			'Shyam': 'Science', 
			'Abdul': 'Hindi'} 

# Printing the subject of Fharan 
print(subjects['Fharan']) 


# # Type Error
# ### An object of an unsupported type is passed as input to an operation or function.

# In[18]:


string = "dams"
num = 4
print(string + num + string)

