#!/usr/bin/env python
# coding: utf-8

# # Prime Number

# In[34]:


# List of numbers to check for primality
check_prime = [26, 39, 51, 53, 57, 79, 85]

# Loop through each number in the list
for prime in check_prime:
    # Check divisors from 2 to one less than the number
    for i in range(2, prime):
        # If the number is divisible by i, it's not a prime number
        if prime % i == 0:
            result = '{} is not a prime number because {} is a factor of {}'.format(prime, i, prime)
            break
        # If no divisors found, the number is a prime number
        if i == prime - 1:
            result = '{} is a prime number'.format(prime)
    # Print the result for the current number
    print(result)

