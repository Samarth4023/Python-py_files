#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = input("Enter your name: ")
print(name)


# In[4]:


name = int(input("Enter your Age: "))
print(name)


# In[3]:


result = eval(input("Enter Any Expression: "))
print(result)


# # Generate Messages

# In[11]:


names = input("Enter Student Name: ").title().split(",")
assignments = input("Enter missing assignments counts: ").split(",")
grades = input("Enter Grade: ").split(",")
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))


# In[ ]:




