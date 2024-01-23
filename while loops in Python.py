#!/usr/bin/env python
# coding: utf-8
while loop in Python:-
It is also a iterative statement but we use while when we don't know the number of times the loop will execute itself.
Syntax:-
1.variable initialization
2.while variable with condition:
    statement(s)
    increment/decrement
While is generally used with complex conditions and not for simple numerical expressions.
It also works on executing the statement when the condition is only True.
# In[4]:


i=int(input("Enter the number: "))
while(i<=3): #while loop
    print(i,end=" ")
    i=i+1


# In[5]:


i=int(input("Enter the Number: "))
while(i>3):
    print("Hello")
    i=i-1
else: 
    print("Bye") #else with while loop.This is executed when the condition above has become False.
    

do while loop in python:-
This concept is not there in Python,here the condition is executed for atleast once and then the condition is checked.
But we can try and implement do-while loop in Python
# In[7]:


i=int(input("Enter the Number: ")) #Implementation of do-while loop 
print(i)
while(i>=3):
    print("Hello") 
    i=i-1


# In[ ]:




