#!/usr/bin/env python
# coding: utf-8

# # for loop with else:-
# Python allows th else keyword with while and for loop too.The else block appears after the body of the loop.The statements with 
# statements in the else block will be executed after all the iterations are completed.

# In[1]:


#Example
for i in range(5):
    print(i)
else:
    print("In the else part of the code") #will be printed after the  completion of the for loop.


# In[2]:


for j in []:
    print(i) #not going in the for loop
else:
    print("Hello")


# In[3]:


for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("In the else part of the code") #here the else part will not be executed as the loop is being breaked at that point.


# In[5]:


i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("In the else part of the code")#here the code will not even execute for i =4 and samely the else part would not print.

