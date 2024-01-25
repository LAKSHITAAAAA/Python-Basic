#!/usr/bin/env python
# coding: utf-8

# # Functions In Python:-
# It is some line of codes written together which can be used repeatively. This saves our efforts to write that same codes repeatively with ease to update and reuse the code.
# So, function is a block of code that performs a specific task whenever it is called.
# # Types Of Functions:-
# 1.Built-in Functions
# 2.User-defined Functions
# Built-in Functions:-
# These are the functions which are pre-defined and coded in the Python language.
# like:-min(),max(),len(),sum(),type(),range(),tuple(),set(),print() and etc.
# User-defined Functions:-
# These are the functions which we can define on our own.We need to define these functions by using the def keyword.
# Syntax:-
# def function_name (parameters):
#     pass #pass can be used when we want to decide the inner code for later.
#     Statement(s)

# In[2]:


def sumofthree(a,b,c): #a function which gives sum of three numbers
    sum=a+b+c
    print(sum)
sumofthree(12,5,8) #calling of the function by writting name of the functions with parameters (if any)


# In[4]:


def average(a,b):
    print((a+b)/2)
average(5,10)


# # Function Arguments and Return Statements:-
# There are 4 types of arguments that we can provide in a function.
# 1.Default Arguments
# 2.Keyword Arguments
# 3.Variable length Arguments
# 4.Required Arguments

# In[10]:


#Default Arguments:-
def average(a=5,b=1): #default arguments for a=5 and b=1
    print((a+b)/2)
average()
average(2,8) #now it will ignore te defalut values of a and b
average(7) #here the value of b will be taken by default which is 1
average(b=11)#here a will take the by default value which is 5


# In[15]:


#Keyword Arguments:-
def sumofthree(a,b=9,c=7): #default values assignment from right to left
    sum=a+b+c
    print(sum)
sumofthree(a=5,c=11) #keyword arguments with key=value format.Here we can even change the order of giving the value of arguments


# In[16]:


#Required Arguments:-
def sumofthree(a,b,c):
    sum=a+b+c
    print(sum)
sumofthree(15,23,6) #here the arguments will be passed in the same order as in the function,that is for a,b and then c.
#here it is required to give all three arguments otherwise it will give an error


# # Variable Length Argument:-
# Sometimew we need to more arguments than those defined in the actual function.The function access the arguments by processing 
# them in the form of tuple.
# There are two ways to achieve the variable length argument.
# 1.Arbitrary Arguments:-
# While creating a function,pass a * before the parameter name while defining the function.The function accesses the arguments
# by processing them in the form of tuple.
# 2.Keyword Arbitrary Functions:-
# While creating a function,pass a * before the parameter name while defining the function.The function accesses the arguments
# by processing them in the form of dictionary.

# In[18]:


def name(*name): #Arbitrary Arguments
    print(name[0],",",name[1],", aur ",name[2],"sabki pasand nirma!! NIRMA!!")
name("Jaya","Sushma","Rekha")


# In[19]:


def average(*numbers): #Keyword Arbitrary Functions giving tuple as an argument
    sum = 0
    for i in numbers:
        sum=sum+i
    print("Avearge is: ",sum/len(numbers))
average(1,5,9,6,78)
    


# In[21]:


def name(**name):#Keyword Arbitrary Functions giving dictionary as an argument
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(mname="Indu",lname="Mati",fname="Rajkumari")


# # Return Statement:-
# The return statement is used to return the value of the expression back to the calling function. 

# In[22]:


def average(*numbers): #Keyword Arbitrary Functions giving tuple as an argument
    sum = 0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=average(1,5,9,6,78) #Here return keyword gives the value which is then stored in the variable c
print(c)

If we write more then one return statement in a single function then the first return is only valid,else are just ignored.