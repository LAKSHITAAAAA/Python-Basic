#!/usr/bin/env python
# coding: utf-8

# # Enumerate Function :-
It is a built-in function in Python that allows you to loop over a sequence (such as list,tuple or string) and get the index 
and value of each element in the sequence at the same time. 
# In[5]:


#Example
fruits=["Apple","Mango","Orange"]
for index,fruit in enumerate(fruits):
    print(index,fruit)
    

Enumerate function returns a tuple containing the index and value of each element in the sequence.By giving two values we 
actually unpack the tuple and assigns every value to a variable.The original tuple has(index,value).
# ## Changing the starting Index
By default,the enumerate function starts at index 0,but you can specify a different starting index by passing it as an 
argument to the enumerate function.
# In[6]:


ice_cream=["Chocolate","Vanilla","Mint Chips","Black Current","Blue berry","Butterscotch"]
for index,flavours in enumerate(ice_cream,start=1): #start=1 specifes that the starting index will be 1
    print(index,flavours)
    


# In[7]:


ice_cream=["Chocolate","Vanilla","Mint Chips","Black Current","Blue berry","Butterscotch"]
for index,flavours in enumerate(ice_cream,start=2): #start=2 specifes that the starting index will be 1
    print(index,flavours)

