#!/usr/bin/env python
# coding: utf-8
if else statements in Python:-
These statements in Python helps in the decision making for any situation.
for multiple if else statements, if elif and else are used.
These are called the conditional statements in technical term.It gives the boolean output on evalution as True or False.
Types of Conditional statements:-
1.if
2.if-else
3.if-elif-else
4.nested if-elif-else,if-else and if
In all these Statements it executes that statement for which the condition is True
For applying these conditional statements,conditional operators are used.
== (used for checking equality of two expressions),>,<,<=,>=
All these operators gives the answer in boolean i.e. True or False
In Python,after these Conditional statements identation(Additional spaces from the beginning) is given which specifies the block of code for that statement.
# In[ ]:


a=int(input("Enter your age ")) #if-else
if a>18:
    print("You can Vote")
else:
    print("You can not Vote")


# In[5]:


b=input("Enter your Name ") #if 
if b=="Lakshita":
    print("Hey Lakshita")


# In[7]:


c=int(input("Enter your marks ")) #if-elif-esle
if c>=90:
    print("Grade=A+")
elif c>=80:
    print("Grade=A")
elif c>=70:
    print("Grade=B+")
elif c>=60:
    print("Grade=C")
else:
    print("Better Luck next time")

