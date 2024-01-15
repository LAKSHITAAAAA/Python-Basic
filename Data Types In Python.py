#!/usr/bin/env python
# coding: utf-8
Variable:-It is like a container which holds data in the RAM (Random Access Memory) of the system when the program is running.Data Type:- It defines the type of data which our variables can store.
#1.Built In Data Types
There are 4 types of data types in Python.
1.Numeric:-int(integer),float(decimal),complex(complex nos.)
2.String:-str(can contain a single or multiple characters)
3.Boolean:-bool(gives True or False as a result)
4.Collection:-A data type which store collection of other data types.Types of Collection data types.
4.1 List[] :- A collection which is mutable(can be changed after the object is created),supports object of different in the same list.But generally has the same elements in a single list.
4.2 Tuple() :- Simliar to list but immutable(cannot be changed after the objects are being created).It can also have mixed type of values.  
4.3 Dictionary{key,value} :-Used to store data in key-value pairs which are ordered (),mutable and do not allow duplicate values or keys.
4.4 Set{values} :-Used to unordered collection with no duplicate values.
Tuples are more memory efficient then Lists as tuples are stored in a single block of memory whereas lists in 2 blocks,one with fixed size stores info about the list objects and second the variable sized block for the data.
# In[1]:


a=1
print(type(a))#int
b=2.0
print(type(b))#float
c=3+6j
print(type(c))#complex
d=True
print(type(d)) #boolean



# In[4]:


mylist=[1,2,3,4] #list
print(mylist)


# In[2]:


t=(1,2,3,4,5,6.6) #tuple
print(t)


# In[5]:


dict={"name":"Lakshita","City":"Indore","State":"MP"}
print(dict)#gives complete dictionary
print(dict["name"]) #gives value corresponding to a particular key


# In[ ]:


s={1,2,3,4,5,6,7} #set
print(type(s))

type is a function that is used to identify the type of object being passed to it as a argument.