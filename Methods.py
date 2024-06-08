#!/usr/bin/env python
# coding: utf-8

# # Methods
# ## Methods are actually functions that are called using dot(.) operator

# ## capitalize()

# In[7]:


my_string = "sebastian thrun"
print(my_string.capitalize())
# it changes the first character of a string to uppercase and converts all other characters to lowercase.


# ## encode()

# In[8]:


my_string = "sebastian thrun"
print(my_string.encode())
# Python String encode() converts a string value into a collection of bytes, using an encoding scheme specified by the user.


# ## casefold()

# In[126]:


my_string = "SEBASTIAN THRUN"
print(my_string.casefold())
# The casefold() method in Python converts a string to lowercase and returns a new string. 
# It is similar to the lower() method, but is stronger and more aggressive.


# ## center()

# In[14]:


my_string = "sebastian thrun"
print(my_string.center(50))
# The center() method in Python is a string method that returns a new string that is centered within a specified width.


# ## count()

# In[23]:


my_string = "sebastian thrun"
print(my_string.count('a'))
# The count() method in Python returns the number of times a specified value appears in a string or a list. 
# It is a built-in method that is available for both strings and lists.


# ## endswith()

# In[40]:


# The endswith() method in Python is used to check if a string ends with a specified suffix.
my_string = "sebastian thrun"
print(my_string.endswith('thrun'))

# -----------OR--------------

my_string = "sebastian thrun"
print(my_string.endswith('a'))

# -----------OR--------------

my_string = "sebastian thrun"
print(my_string.endswith('n'))


# ## expandtabs()

# In[48]:


my_string = "sebastian \tthrun"
print(my_string.expandtabs(20))
# The expandtabs() method in Python is a string method that replaces all occurrences of tab characters (\t)
# in a string with a specified number of spaces.


# ## find()

# In[53]:


# The find() method in Python is a string method that returns the lowest index value of the first occurrence of the substring from the input string; 
# else it returns -1.
my_string = "sebastian thrun"
print(my_string.find('thrun'))

#-------------OR-------------

my_string = "sebastian thrun"
print(my_string.find('Sebastian'))

# -----------OR--------------

my_string = "sebastian thrun"
print(my_string.find('sebastian'))


# ## format()

# In[56]:


# The format() method in Python is a string method that allows you to format a specified value(s) and insert them inside the string's placeholder. 
# The placeholder is defined using curly brackets: {}. 
pi = 3.14159
print("The value of pi is: {}".format(pi))


# ## format_map()

# In[65]:


# Python format_map() returns a new string by concatenating the values in the user-supplied dict within the defined places. 
# This approach uses the placeholder ({}) formatting style. This format_map() function is used to returns a dictionary key's value.
a = {'x':'Mike', 'y':'Perry'}
b = {'x':'Sam', 'y':'Jimmy'}

print("That DJ is {x} {y}".format_map(a))
print("That DJ is {x} {y}".format_map(b))


# ## index()

# In[70]:


#The index() method in Python is a built-in function that returns the index of the first occurrence of a specified value within a list. 
#It takes one argument, which is the value to search for. 
#If the value is found in the list, the index() method returns the index of the first occurrence. 
#If the value is not found in the list, the index() method raises a ValueError exception.
my_string = "sebastian thrun"
print(my_string.index('thrun'))


# ## isalnum()

# In[73]:


# The isalnum() method in Python is a string method that returns True if all characters in a string are alphanumeric. 
# Alphanumeric characters include: Alphabet letters (a-z) and Numbers (0-9).
# Characters that are not alphanumeric include: Space ! * # & % ?

my_string = "sebastia98thrun"
print(my_string.isalnum())

#-------------OR--------------

my_string = "sebastia98thrun&"
print(my_string.isalnum())


# ## isalpha()

# In[79]:


# The isalpha() method in Python is used to check if a string contains only alphabetic characters. 
# It returns True if all the characters in the string are alphabetic and False if not.

my_string = "sebastia98thrun"
print(my_string.isalpha())

my_string = "sebastianthrun"
print(my_string.isalpha())

my_string = "sebastian thrun"
print(my_string.isalpha())


# ## islower()

# In[83]:


# The islower() method returns True if all the characters are in lower case, otherwise False. 
# Numbers, symbols and spaces are not checked, only alphabet characters.

my_string = "sebastian thrun"
print(my_string.islower())


# ## istitle()

# In[88]:


# The istitle() method in Python is a built-in string method that checks if a string is title-cased. 
# A title-cased string is a string where all words start with a capital letter and the rest of the letters are lowercase. 
# The istitle() method ignores whitespace characters, numbers, and symbols.

my_string = "sebastian thrun"
print(my_string.istitle())

my_string = "Sebastian Thrun"
print(my_string.istitle())


# ## isdecimal()

# In[127]:


# The isdecimal() method in Python is a built-in function that returns True if all the characters in a string are decimals (0-9). 
# The method can also be used on unicode objects.

my_string = "34526754"
print(my_string.isdecimal())

my_string = "34526754.965"
print(my_string.isdecimal())

my_string = u"34526754"
print(my_string.isdecimal())

my_string = "345 26754"
print(my_string.isdecimal())


# ## isnumeric()

# In[95]:


# Python isnumeric() method returns True if all of the characters in the string are numeric (only numbers). 
# If not, it returns False. 
# The Python isnumeric() function returns a Boolean value depending on the existence of numeric characters in the string.

my_string = "34526754"
print(my_string.isnumeric())

my_string = "python34526754"
print(my_string.isnumeric())

my_string = "34526754.963"
print(my_string.isnumeric())

my_string = "34526 754"
print(my_string.isnumeric())


# ## isupper()

# In[99]:


# The isupper() method in Python is a built-in method used for string handling. 
# This method returns “True” if all characters in the string are uppercase, otherwise, returns “False”. 
# It returns “True” for whitespaces but if there is only whitespace in the string then returns “False”.

my_string = "SAM"
print(my_string.isupper())

my_string = "SA    M"
print(my_string.isupper())

my_string = "Sam"
print(my_string.isupper())

my_string = "    "
print(my_string.isupper())


# ## isdigit()

# In[103]:


# The isdigit() method in Python is a string method that checks if all characters in a string are digits. 
# It returns True if all characters are digits, and False otherwise.

my_string = "12345"
print(my_string.isdigit())

my_string = "12345abcd"
print(my_string.isdigit())

my_string = "12345.789"
print(my_string.isdigit())


# ## isprintable()

# In[128]:


# The isprintable() method in Python is a built-in string method that checks if a string contains any printable characters. 
# It returns True if all characters in the string are printable, or if the string is empty. 
# Otherwise, it returns False. Printable characters are those that can be displayed on a screen or printed on paper. 
#They include letters, numbers, symbols, punctuation, and whitespace.

my_string = "12345"
print(my_string.isprintable())

my_string = "sam"
print(my_string.isprintable())

my_string = " "
print(my_string.isprintable())

my_string = "\n"
print(my_string.isprintable())


# ## join()

# In[109]:


# The join() method in Python takes all items in an iterable and joins them into one string. 
# A string must be specified as the separator.

fruits = ['apple', 'banana', 'cherry']
string = ','.join(fruits)
print(string)

numbers = ('1', '2', '3')
string = ' '.join(numbers)
print(string)


# ## isidentifier()

# In[114]:


# The isidentifier() method in Python checks if a string is a valid identifier. 
# The method returns True if the string is valid and False if it is not.

my_string = "sam"
print(my_string.isidentifier())

my_string = "12sam"
print(my_string.isidentifier())

my_string = "sam jhon"
print(my_string.isidentifier())

my_string = "sam_jhon"
print(my_string.isidentifier())


# ## isspace()

# In[120]:


# The isspace() method in Python returns True if all the characters in a string are whitespaces, and False otherwise.

my_string = "sam jhon"
print(my_string.isspace())

my_string = "samjhon"
print(my_string.isspace())

my_string = " "
print(my_string.isspace())

my_string = "  s  "
print(my_string.isspace())


# ## ljust()

# In[125]:


# The ljust() method in Python is used to left-align a string. 
# It takes two arguments: the length of the string and the character to use for padding. 
# If the length of the string is less than the length specified, the padding character will be added to the right of the string. 
# If the length of the string is greater than the length specified, the string will be truncated.

my_string = "sam"
print(my_string.ljust(20))

my_string = "sam"
print(my_string.ljust(20, '*'))


# ## split()

# In[12]:


# The split() method in Python is a string method that splits a string into a list of strings, where each string is a substring of the original string. 
# The split() method takes two arguments: a separator and a maximum number of splits. 
# The separator is a string that is used to split the original string. 
# The maximum number of splits is an integer that specifies the maximum number of times the split() method will split the original string.

my_string = "The Cow jumped over the moon"
print(my_string.split(' ', 5))

my_string = "The Cow jumped over the moon"
print(my_string.split(' ', 3))

my_string = "The Cow jumped over the moon"
print(my_string.split(' '))


# # Each of these methods accepts string
# # Methods that are possible with any string
