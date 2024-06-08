#!/usr/bin/env python
# coding: utf-8

# # Default Arguments

# In[3]:


def cylinder_volume(height, radius = 5):    # here 5 is default while running

    print(cylinder_volume(10, 5))           # we can anything here (It's same)
    print(cylinder_volume(10))

#----------------OR------------------
    print(cylinder_volume(10, 7))           # we can still change argument as it is declared above 5

# Code will run radius 7 (i.e., we are overriding the default value 5)


# ## It is possible to pass values by 2 ways.
# ## 1) Position
# ### - print(cylinder_volume(10, 7))
# ## 2) Name
# ### - print(cylinder_volume(height = 10, radius = 7))

# 

# # Defining Functions
# ## 1) Population Density Functions.

# In[7]:


def population_density(population, land_area):
    return population / land_area

test1 = population_density(10, 1)
expected_result1 = 10
print('expected result: {}, actual result: {}'.format(expected_result1, test1))

test2 = population_density(864816, 121.6)
expected_result2 = 7123.6902801
print('expected result: {}, actual result: {}'.format(expected_result2, test2))


# ## 2) Time Delta.

# In[9]:


def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))

