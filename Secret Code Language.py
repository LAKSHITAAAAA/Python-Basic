#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=input("Enter the string you want to Encode!  ")
def encode(a):
    if(len(a)>=3):
        c=a[1:]
        d=c+a[0]
        e="a"+"e"+"i"+d+"m"+"o"+"r"
        print(e[0:])
    else:
        print(a[-1:-(len(a)+1):-1])
encode(a)


# In[2]:


b=input("Enter the string you want to Decode! ")
def decode(b):
    if(len(b)<3):
        print(b[-1:-(len(a)+1):-1])
    else:
        c=b.rstrip("r")
        #print(c)
        d=c.rstrip("o")
        #print(d)
        e=d.rstrip("m")
        #print(e)
        f=e[3:]
        #print(len(f))
        print(f[-1]+f[0:(len(f)-1)])        
decode(b)

