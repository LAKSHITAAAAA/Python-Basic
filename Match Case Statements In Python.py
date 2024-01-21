#!/usr/bin/env python
# coding: utf-8
Match Case Statements:-
It is basic addition in Python after 3.10 edition
It is similiar to switch case in C/C++

# In[3]:


x=int(input("Enter the Number "))
match x:
    case 0:
        print("X is Zero")
    case 1:
        print("X is One")
    case 4:
        print("X is four")
    case _: #case _ is used for showing the default case. there can be more than one default case in every program.
        #In C/C++ it was necessary to use break after each statement which is not complusory in Python.
        print("The number is 3 or other")

match case is more powerful than if else as if else just relies on True or False values but match case can check for patterns
as well.
and match case is faster than if else statement as it continously compares the variables or patterns,whereas in if else we need to take the variable again and again to check the condition.