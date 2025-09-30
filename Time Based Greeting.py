#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Question On if-else
import time as t
t1=t.strftime('%H:%M:%S') #The strftime() converts the current time in the specified format in string datatype.
if(t1>='16:00:00'):
    print("Good Evening")
elif(t1>='12:00:00' and t1<'16:00:00'):
    print("Good Afternoon")
else:
    print("Good Morning")
    


# In[ ]:




