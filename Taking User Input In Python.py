#!/usr/bin/env python
# coding: utf-8
Taking Input from User In Python:-
we use input() function for taking input. It takes everything as a string when passed to it, which can be explicility typecasted later.
# In[4]:


a=input("Enter a ")
print(type(a)) #by default string 
b=int(input("Enter b "))
print(type(b)) #int
c=float(input("Enter c "))
print(type(c)) #float
#similarly can be typecasted to other data types as well.


# In[9]:


x=input("Enter a ")
y=input("Enter b ")
print(x+y)
#print(x*y) error
#print(x-y) error
#print(x/y) error


# In[ ]:




