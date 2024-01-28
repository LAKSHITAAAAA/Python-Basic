#!/usr/bin/env python
# coding: utf-8

# # f-Strings In Python:-
# f-String is one such way in Python which provides a way to place variables conveniently inside the strings.
# This functionality is available after the Python 3.6 version.
# It is used for string formatting.

# In[3]:


# an example of string formatting.
letter="Hey I am {} and I am from {}"
name="Lakshita"
address="India"
print(letter.format(name,address)) # formatting of the string by using format() method.By giving arguments, we are giving them 
#as an input and will be assigned in that particular order only.i.e name for the first bracket and address for 
#the second bracket 


# In[4]:


#but if we swap the arguments then, it will print in that order only ,which is wrong
print(letter.format(address,name))



# In[7]:


#One way to rectify this problem is as shown;
#letter="Hey I am {name} and I am from {address}"#this gives error here
letter=Hey I am {1} and I am from {0}
name="Lakshita"
address="India"
print(letter.format(address,name))

This was how formatting was done before Python 3.6 version. This is method which was useful at that time, but is not convenient
now-a-days.As in this method there is so much to write and understand as well.
# In[6]:


#now solution to this;
print(f"Hey I am {name} and I am from {address}") #f-string allows placing variables inside of a string.We do that by using {}


# In[8]:


txt="For only {price:.2f} dollars!!"
print(txt.format(price=49.099054654)) # will print only upto 2 decimal places, because .2f also by rounding it off


# In[10]:


price=49.09865473
txt=f"For Only {price:.3f} dollars!!"
print(txt)


# In[11]:


print(f"Hey I am {{name}} and I am from {{address}}") #double {{}} to use the content as it is.


# In[ ]:




