#!/usr/bin/env python
# coding: utf-8
Loops in Python are used to repeat a particular statement(s) until a certain condition.
Types of loops:-
1. for loop
2. while loopfor loop:-
for loops can iterate over a sequence of iteratble objects (which can be used in looping) in Python.Iterating over a sequence is nothing but iterating over strings,lists,tuples,sets and dictionary.
Syntax:-
for (variable) in range("Specified Range"):
    condition(s)
or
for (variable) in (another variable of iterable objects):
    condition(s)
# In[1]:


name="Lakshita" #for loop for strings
for i in name:
    print(i,end=",") #end is used to place a separator at the end of each iteration and then it doesn't go to default new line


# In[2]:


name="Lakshita"
for i in name:
    print(i)


# In[4]:


a=["Red","Green","Blue","Yellow"] #for loop for lists
for x in a:
    print(x)

# range():- It is a function used to generate a sequence of numbers.
syntax:- range("Starting_value","Ending_Value","Step") # It gives output as ending_value-1
#Step:-it specifies the duration og gap between two numbers.By default it is 1.
# In[6]:


for i in range(5):#prints 0 to 4
    print(i,end=" ")


# In[ ]:




