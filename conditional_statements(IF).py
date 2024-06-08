#!/usr/bin/env python
# coding: utf-8

# # If

# In[4]:


# Initialize phone balance and bank balance
phone_balance = 3
bank_balance = 100

# Print the initial balances
print("Initial balances:")
print("Phone balance:", phone_balance)
print("Bank balance:", bank_balance)

# Check if phone balance is less than 5
if phone_balance < 5:
    # Top up phone balance by 10
    phone_balance += 10
    # Deduct 10 from bank balance
    bank_balance -= 10

# Print updated balances
print("Updated balances:")
print("Phone balance:", phone_balance)
print("Bank balance:", bank_balance)


# # If Else

# In[21]:


# Initialize phone balance and bank balance
phone_balance = 9
bank_balance = 100

# Print the initial balances
print("Initial balances:")
print("Phone balance:", phone_balance)
print("Bank balance:", bank_balance)

# Check if phone balance is less than 5
if phone_balance < 5:
    # Top up phone balance by 10
    phone_balance += 10
    # Deduct 10 from bank balance
    bank_balance -= 10
    # Print updated balances
    print("Updated balances:")
    print("Phone balance:", phone_balance)
    print("Bank balance:", bank_balance)

else:
    # Print Initial unchanged balances
    print("Original balances:")
    print("Phone balance:", phone_balance)
    print("Bank balance:", bank_balance)
    


# # Boolean Expressions

# ### logic + algebra (Checking only one condition)

# In[64]:


# Calculate BMI based on weight and height
weight = 70     # Weight in kilograms  
height = 1.75   # Height in meters
# Calculate BMI using the formula: BMI = weight / (height^2)
if 18.5 <= (weight / height ** 2) < 25:                         # Check if the calculated BMI falls within the normal range (18.5 to 24.9)  
    print("BMI is considered as Normal !")


# ### logical opertors

# In[72]:


is_raining = 1
is_sunny = 1
if is_raining and is_sunny:
    print('Is there a Ranibow')


# ### multiple

# In[95]:


not_unsubscribed = 1               # this code will print the output because loaction and not_unsubscribed satisfies the condition
location = 'IND'
if (not_unsubscribed) and (location == 'USA' or location == 'IND'):
    print('send email')


# In[89]:


not_unsubscribed = 0               # this code snippet will not print any output as not_unsubscribed is 0
location = 'IND'
if (not_unsubscribed) and (location == 'USA' or location == 'IND'):
    print('send email')


# In[93]:


not_unsubscribed = 1               # this code snippet will not print any output as location is RUS and not USA or IND
location = 'RUS'
if (not_unsubscribed) and (location == 'USA' or location == 'IND'):
    print('send email')


# ## NOTE: Do not evaluate truth value of boolean variable with "==" because the variable itself is a boolean expression.
