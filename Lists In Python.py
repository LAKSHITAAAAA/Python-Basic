#!/usr/bin/env python
# coding: utf-8

# # Lists In Python:-
# We make list when we want to store multiple things under a single variable
# 1.Lists are ordered collection of data items.By order we mean that items will be printed in the same order as they were written.
# 2.They store multiple items in a single variable.
# 3.List items are separated by commas and enclosed within brackets[]
# 4.List are changeable; we can alter them after creation.

# In[7]:


#Examples of List:-
list1=[1,2,3,4,5,6,7,8,9]
list2=["Red","Green","Blue","Orange","Purple"]
list3=["Abhijeet",18,"Riya",9.9] #different data types together in a single list
print(list1)
print(list2)
print(list3)
print(list3[0],"is in",list2[2],"house") #accesing elements by using indexes(here positive in this case)
print(list1[-2])#negative indexing


# # Operations on List:-
# 1.in keyword:- To check that a particular element is in list or not.
# 2.Slicing on List:- listname[Start:End:Jump]
# 

# In[12]:


#in keyword
l=[1,2,3,4,5]
if 5 in l: #in keyword
    print("Yes")
else:
    print("No")
print(l[1:4:2]) #slicing on List
print(l) #prints the complete list
print(l[:]) #prints the complete list


# # List Comprehension:-
# List Comprehensions are used for creating new lists from other iterables like lists,tuples,dictionaries,sets and even arrays and strings.

# In[15]:


names=["Lakshita","A","B","C","D","E"]
with_i=[item for item in names if "L" in item] #List Comprehension
print(with_i)


# # List Methods:-
# 1.list.sort():-This method sorts the list in ascending order.The original list is updated.
# 2.list.append("element"):-This method adds the given element at the last of the list.he original list is updated.
# 3.list.reverse():- prints the original order of the list in reverse.
# 4.list.index("element"):-prints the index of the given element for it's first occurence.
# 5.list.count("element"):-prints the number of times the given element occurs in the list.
# 6.list.copy():-Returns copy of the list.This can be done to perform operations on the list without modifying the original list.
# 7.list.insert("index","element"):-Inserts the item at the given index.User has to specify the index and the item to be inserted within the insert() method.
# 8.list.extend(list2):-This method adds an entire list or any collection datatype (set,tuple,dictionary) to the exisiting list.
# The output simply adds the contents of list2 after the ending of list.
# 9.
# 

# In[10]:


l=[9,8,5,7,66,4,56,23]
l.sort() #sort method
print(l)
l.sort(reverse=True) #sort the list in reversal order 
print(l)
l.append(54)#append method
print(l)
l.reverse()
print(l)
print(l.index(56))


# In[13]:


l=[1,2,3,5,6,5,8,5,4,9,98,9,11]
m=l.copy()
m[0]=25
print(m) #prints the modification done on the list.
print(l) #prints the original list.
l.insert(8,33) #inserting 33 at 8th index.
print(l)


# In[19]:


l10=[1,2,3,4,5]
l20=[6,7,8,9,10]
l10.extend(l20)
print(l10) #prints both the list after extend() into a single list.
print(l20)
l20.extend(l10)
print(l20) #prints the list which was already modified with the new extension afer using the extend()


# In[20]:


a=[1,2,3]
b=[4,5,6]
l=a+b
print(l) #this concatination by using "+" operator

extend()is a method in list for joining or concating two lists,whereas "+" is a operator for joining two lists.
# In[ ]:




