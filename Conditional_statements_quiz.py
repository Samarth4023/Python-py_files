#!/usr/bin/env python
# coding: utf-8

# # Quiz

# ## 1) Factorial (!) 

# In[5]:


# While Loop
# Initialize variables
number = 6
product = 1
current = 1

# While loop: Multiply the product by each integer from 1 to 'number'
while current <= number:
    # Multiply the 'product' by the current integer
    product *= current
    # increment current integer by 1
    current += 1

# Print the final product
print(product)


# In[6]:


# For Loop
# Initialize variables
number = 6
product = 1

# Iterate through a range of integers from 2 to 'number' (inclusive)
for i in range(2, number + 1):
    # Multiply the 'product' by the current integer 'i'
    product *= i

# Print the final product
print(product)


# ## 2) Count By

# In[8]:


# Initialize variables
start_num = 1
end_num = 11
count_by = 1

# Initialize break_num with start_num
break_num = start_num

# Increment break_num until it exceeds end_num
while break_num <= end_num:
    break_num += count_by

# Print the final value of break_num
print(break_num)  # Output: 12


# ## 3) Count By Check

# In[10]:


# Initialize variables
start_num = 13
end_num = 11
count_by = 1

# Initialize break_num with start_num
break_num = start_num

# Check if start_num is greater than end_num
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than end value."
else:
    # Increment break_num until it exceeds end_num
    while break_num <= end_num:
        break_num += count_by
        result = break_num

# Print the result (either an error message or the final value)
print(result)  # Output: Oops! Looks like your start value is greater than end value.


# ## 4) Nearest Square

# In[12]:


# Set the limit for finding the nearest square
limit = 40

# Initialize a variable to keep track of the current number
num = 0

# Iterate until the square of (num + 1) is less than the limit
while (num + 1) ** 2 < limit:
    num += 1

# Calculate the nearest square
nearest_square = num ** 2

# Print the result
print(nearest_square)


# ## Code Block

# In[21]:


# Given list of numbers
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Initialize variables to keep track of odd numbers and their sum
count_odd = 0
list_sum = 0

# Initialize an index variable for iterating through the list
i = 0

# Calculate the length of the list
len_num_list = len(num_list)

# Iterate through the list
while (count_odd < 5) and (i < len_num_list):
    # Check if the current number is odd
    if num_list[i] % 2 != 0:
        # If odd, add it to the sum
        list_sum += num_list[i]
        # Increment the count of odd numbers
        count_odd += 1
    # Move to the next element in the list
    i += 1

# Print the total count of odd numbers and their sum
print("Number of odd elements:", count_odd)
print("Sum of odd elements:", list_sum)

