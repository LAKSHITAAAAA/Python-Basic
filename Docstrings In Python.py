#!/usr/bin/env python
# coding: utf-8

# # Docstrings In Python:-
# Python Docstrings are the string literals that appear right after the definition of a function,method,class or module.
# It is the explanatory details about the code that is being written.
# """kjwdhgfuh""" is the way of representing the docstring.
# "#" is used for comments in the python code.
# Comments are used for telling the improvement in the future about the code.
# Docstrings and comments are two different things, they are not the same.
# Comments are ignored by the interpreter whereas docstrings are not.

# In[2]:


def square(n):
    '''Take in a number n,returns the square of n''' #Docstring
    print(n**2)
square(5)
print(square.__doc__) #this gives the document given by using docstrings


# # PEP-8:-
# PEP stands for Python Enhancement Proposal
# PEP-8 is a document that provides guidelines and best practices on how to write the Python code.
# It was written in 2001.The primary focus of PEP-8 is to improve the readability and consistency of the Python code.

# In[3]:


import this #this is a easter egg in Python which is a poem type thing that tells us about how to write efficient Python code.
#the name of this poem is "The Zen Of Python !"


# In[ ]:




