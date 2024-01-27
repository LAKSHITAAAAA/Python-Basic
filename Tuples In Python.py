#!/usr/bin/env python
# coding: utf-8

# # Tuples In Python:-
# Tuples are ordered collection of data items.They store multiple items in a single variable.Tuple items are separated by commas and ().Tuples are unchangeable meaning we can not alter them after creation.
# Tuple also supports slicing.

# In[9]:


t=(1,2,3,"Lakshita",2.5) #same and different types of datatypes together.
print(type(t))
print(t[0])#we can access those elements by using indexing but can't change them 
if ("Lakshita" in t): #in keywird is used to check occurence
    print("Yes")
else:
    print("No")
print(t[0:4:2]) #Slicing On Tuples


# In[8]:


tup=(1,) #a single element tuple with comma(necessary)
print(type(tup))
print(len(tup)) #prints length of the tup by using len()


# # Operations On Tuples:-
# There are no particular functions for updating a tuple that has been made already.We need to convert the tuple into list to 
# perfrom operation son that particular tuple's data.But we can concat two lists as we are making a new tuple here and not 
# changing the original tuples. However,there are some tuple specific methods;
# 1.tuple.count(Element):- It gives the count of the given element in the tuple.
# 2.tuple.index(element,start,end):- Returns the first occurence of the given element form the tuple.This method raises an error
# a ValueError if the element is not found in the tuple.
# 3.tuple.len():- Returns length of the tuple.
# 
# 

# In[14]:


c=("Spain","Russia","Japan","Germany","India")
temp=list(c)
temp.append("China") #adding item
print(temp)
temp.pop(3) #removing item
print(temp)
temp[2]="Finland" #changing item
c=tuple(temp)
print(c)


# In[17]:


t1=(1,5,9,7,5,3,52)
t2=(5,47,6,9,5,8)
t3=t1+t2 #concating two tuples
print(t3)
print(len(t3))


# In[ ]:




