#!/usr/bin/env python
# coding: utf-8
Typecasting In Python:-
It is a process of converting a data type to another data type.
There are 2 types of typecasting:-
1.Implicit Conversion:-Conversion done by Python itself
2.Explicit Conversion:-Conversion done by the Programmer
# In[2]:


a=int(input("Enter the Number"))
b=2.5
c=a+b#Implicit Conversion int to float automatically
print(c)
print(type(c))


# In[5]:


a=input("Enter number 1 ")
b=input("Enter number 2 ")
print(type(a))
c=int(a)+int(b) #Explicit Conversion from string to integer
print(c)
print(type(c))


# In[ ]:




