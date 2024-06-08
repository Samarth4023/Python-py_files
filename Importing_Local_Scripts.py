#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the module named "other_script"
import other_script

# Print the value of the variable "rum" from the imported module
print(other_script.rum)


# # Try It Out!

# In[3]:


# Import the module named "useful_functions" and give it an alias "uf"
import useful_functions as uf

# Given a list of student scores
scores = [88, 92, 79, 93, 85]

# Calculate the mean of the original scores
mean = uf.mean(scores)

# Apply a curve by adding 5 to each score
curved = uf.add_five(scores)

# Calculate the mean of the curved scores
mean_c = uf.mean(curved)

# Print the original scores, original mean, and new mean
print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

# Print the value of the __name__ variable for the current module
print(__name__)

# Print the value of the __name__ variable for the imported module "useful_functions"
print(uf.__name__)


# # useful_functions.py

# In[5]:


# Define a function to calculate the mean of a list of numbers
def mean(num_list):
    return sum(num_list) / len(num_list)

# Define a function to add 5 to each element in a list
def add_five(num_list):
    return [n + 5 for n in num_list]

# Main function for testing
def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

# Execute the main function if this script is run directly
if __name__ == '__main__':
    main()

