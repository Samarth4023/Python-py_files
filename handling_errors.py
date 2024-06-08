#!/usr/bin/env python
# coding: utf-8

# # Try statement

# In[1]:


# Prompt the user to input a number
try:
    x = int(input("Enter your Number: "))
except:
    # If the input is not a valid integer, print an error message
    print("That's not a valid Number !")


# # Try statement with while loop

# In[3]:


# Continuously prompt the user to input a number until a valid integer is provided
while True:
    try:
        x = int(input("Enter your Number: "))
        break  # Exit the loop if a valid integer is entered
    except:
        print("That's not a valid Number !")  # Print an error message if the input is not a valid integer
    print("Attempted Input !")  # This line will execute after each input attempt


# # finally block

# In[5]:


# Continuously prompt the user to input a number until a valid integer is provided
while True:
    try:
        x = int(input("Enter your Number: "))
        break  # Exit the loop if a valid integer is entered
    except:
        print("That's not a valid Number !")  # Print an error message if the input is not a valid integer
    finally:
        print("Attempted Input !")  # This line will execute after each input attempt


# # adjust particular exception

# In[17]:


while True:
    try:
        x = int(input("Enter your Number: "))
        break
    except (ValueError, KeyboardInterrupt):
        print("That's not a valid Number !")
    #except ValueError:
        #print("That's not a valid Number !")
    #except KeyboardInterrupt:
        #print("zzzz !")
        #break
    finally:
        print("Attempted Input !")


# # Practice Quiz 
# ## try n except

# In[7]:


def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Warning! Please input a different number of people.")
    
    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':
    
    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))
   
    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")


# In[ ]:




