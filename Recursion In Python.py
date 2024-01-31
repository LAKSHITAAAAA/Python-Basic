#!/usr/bin/env python
# coding: utf-8

# # Recursion In Python:-
# It is the process of defining something in terms of itself.
# In programming, it is defined as the function calling itself.

# In[4]:


#Example of factorial
def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return (num * factorial(num-1))
#Driver Code
num=7
print(num)
print("The factorial of the given number is: ",factorial(num))


# In[6]:


#Example of fib Series
def fib(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fib(n-1)+fib(n-2))
#Driver Code
n=6
print(n)
print("The",n,"th term of fib series is: ",fib(n))

