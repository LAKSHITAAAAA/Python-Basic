#!/usr/bin/env python
# coding: utf-8

# # Sets In Python:-
# These are those type of data structures which holds only unique values or no duplicate values.These are unordered collection of data items.
# They store multiple items in a single variable.Set items are seperated by commas and enclosed within curly brackets{}.
# Sets are unchangeable.

# In[6]:


a={'Lakshita',19,False,5.9,19}
print(a)
print(type(a))
b={} #empty set gives dictionary as the output after calling the type() function.
print(type(b))
c=set() #Process of making an empty set
print(type(c))
for i in a:
    print(i,end=" ")


# # Methods Of Sets:-
# 1.set3=set.union(set2):-Here the set3 is the new set made which contains all the elements of set and after that set2 but not in any particular order.Here the original sets remains unchanged.
# 2.set.update(set2):-Here the set will change permanently after the update operation.
# 3.set.intersection(set2):-Here the elements common to both the sets will be printed.
# 4.set.intersection_update(set2):- Here the intersection elements will get now stroed into set
# 5.set.symmetric_difference(set2):- (A union B) - (A intersection B).
# 6.set.difference(set2):- will be set-set2.
# 7.isdisjoint():-Returns boolean value and true when two sets have nothing in common.
# 8.issuperset():-Returns boolean value and true when bigger set contains all the elements of the other set.
# 9.issubset():-Returns boolean value and true when smaller set contains all the elements of the other set.
# 10.add():- for adding a single element in the set.
# 11.remove()/discard():-for removing the elements from the set.
# 12.pop():-Returns and removes the last element of the set,but we don't know the last element of the set.
# 13 del:- It is a keyword used for deleting an entire set.
# 14.clear():- It just deletes the elements of the set and not the complete set.
# 

# In[12]:


s={12,3,56,89}
s2={25,36,95,78}
s3=s.union(s2)
print(s3)
print(s,s2) #s and s2 remains the same even after the union operation is performed.
s.update(s2)
print(s) #now the values of the set are permanently updated by the values of s2


# In[19]:


s4={1,2,5,6,8,9,8,9,45}
s5={24,36,55,35,3,8,9}
s6=s4.intersection(s5)
print(s6)


# In[28]:


sa={1,2,3,4,5,6}
sb={3,4,5,6,7,8,9}
sb.intersection_update(sa)
print(sb)
print(sa)
sd=sb.symmetric_difference(sa)
print(sd)
c=sd.difference(sb)
print(c)


# In[35]:


sa={1,2,3,4,5,6}
sb={3,4,5,6,7,8,9}
print(sa.isdisjoint(sb))
print(sa.issuperset(sb))
print(sa.issubset(sb))
sa.add(588)
print(sa)
sa.remove(6)
print(sa)
print(sa.pop())

Difference between remove() and discard() is that on not finding the element to be deleted on the set which is given as an 
argument remove() raises an error whereas discard does not. 