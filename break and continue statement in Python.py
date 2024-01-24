#!/usr/bin/env python
# coding: utf-8
break:-
when we want to break the further processing of any loop then we use break statement.
continue:-
when we don't want to terminate the whole loop but on a particular condition we want the loop to go on.
# In[2]:


print("The Multiplication Table of 5:- ")
for i in range(12):
    if(i==10):
        break #break statement
    print("5 X",i+1,"= ",5*(i+1))


# In[5]:


print("The Multiplication Table of 5:- ")
for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue #continue statement
    print("5 X",i,"= ",5*(i))


# In[9]:


#Emulation of do-while loop
i=0
while True:
    print(i,end=" ")
    i=i+1
    if(i%100 == 0):
        break


# In[ ]:




