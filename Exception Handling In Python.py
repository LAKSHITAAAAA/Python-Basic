#!/usr/bin/env python
# coding: utf-8

# # Exception Handling In Python:-
# Exception Handling is the process of responding to unwanted or unexcepted events when a computer program runs.Exception
# handling deals with these events to avoid the program or system crashing.
# Python has many built-in exceptions that are raised when the program encounters an error.
# When these exceptions occur,the python interpreter stops the current process and passes it to the category of calling process
# until it is handled.If not,the program will crash.

# # try.... except blocks :-
# try... except blocks are used in Python to handle errors and exceptions.The code in try block runs when there is no error.
# If the try block catches an error,then the except block is executed.

# In[3]:


# Example
a=input("Enter the number: ")
print("Multiplication Table of ",a,"is: ")
try:
    for i in range(1,11):
        print(f"{int (a)} X {i}= {int(a)*i}")
except Exception as e:
    print(e)
    
print("Out of the exception handling block")


# In[8]:


#handling a specific error
# we can also use except in a single code
try:
    a=int(input("Enter the number: "))
    b=[6,3,5]
    print(b[a])
except ValueError:
    print("Enter a number!")
except IndexError:
    print("Index Error!")


# # finally clause:-
# Everything written in the finally block is always exxecuted whether there is an error or not.
# It is used as try...except... and then finally...
# It can be used for concluding the overall execution of the program.

# In[11]:


# Example
try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(a/b)
except ValueError:
    print("Enter an integer only!")
except ZeroDivisionError:
    print("Division By Zero!")
finally:
    print("The program is completed")

One of the Important use cases of finally block is in a function which returns a value.
# # Raising Custom Errors:-
# We can raise custom errors by using the raise keyword.

# In[12]:


#Example
salary=int(input("Enter salary Amount: "))
if not 20000<salary<50000:
    raise ValueError("Not a Valid Salary!")

