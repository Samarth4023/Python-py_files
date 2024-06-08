#!/usr/bin/env python
# coding: utf-8

# # Specific Errors
# ## ZeroDivisionError occurred: integer division or modulo by zero

# In[1]:


# Define a function called "party_planner" to calculate cookie distribution
def party_planner(cookies, people):
    # Initialize variables for leftovers and cookies per person
    leftovers = None
    num_each = None

    try:
        # Calculate the number of cookies each person will get
        num_each = cookies // people
        # Calculate the remaining cookies (leftovers)
        leftovers = cookies % people
    except ZeroDivisionError as e:
        # Handle the case when the number of people is zero
        print("ZeroDivisionError occurred: {}".format(e))

    # Return the results
    return num_each, leftovers

# Initialize a flag for party continuation
lets_party = 'y'

# Continue party planning until the user decides to stop
while lets_party == 'y':
    # Get input from the user: number of cookies and number of people
    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    # Calculate cookie distribution using the party_planner function
    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # If cookies_each is not None (i.e., people > 0)
        # Print the party details
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    # Ask if the user wants to continue party planning
    lets_party = input("\nWould you like to party more? (y or n) ")


# # No Specific Errors
# ## except Exception as e:

# In[3]:


# Define a function called "party_planner" to calculate cookie distribution
def party_planner(cookies, people):
    # Initialize variables for leftovers and cookies per person
    leftovers = None
    num_each = None

    try:
        # Calculate the number of cookies each person will get
        num_each = cookies // people
        # Calculate the remaining cookies (leftovers)
        leftovers = cookies % people
    except Exception as e:
        print("Exception occurred: {}".format(e))

    # Return the results
    return num_each, leftovers

# Initialize a flag for party continuation
lets_party = 'y'

# Continue party planning until the user decides to stop
while lets_party == 'y':
    # Get input from the user: number of cookies and number of people
    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    # Calculate cookie distribution using the party_planner function
    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # If cookies_each is not None (i.e., people > 0)
        # Print the party details
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    # Ask if the user wants to continue party planning
    lets_party = input("\nWould you like to party more? (y or n) ")

