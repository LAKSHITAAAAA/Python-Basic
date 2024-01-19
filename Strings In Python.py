#!/usr/bin/env python
# coding: utf-8
#Strings In Python:-
In Python,a string is data type which stores collection of characters together.It is enclosed with "" or ''.
It is used when we store the unicode characters(An International standard that defines all characters and makes characters accessible across platforms,programs and devices) in our program.
It is a sequence or array of textual data.

# In[5]:


a="Lakshita" #making a string
b=' Mukati'
print(type(a))
print(a+b) # + operator is adding two strings

Multiline string by using """hvedhv"""
# In[7]:


a="""He said hii
I also said hii
then we went to play football
after that I went back to my home"""  #''' sdfvkHSGd''' can also be used in place of '''dhvgiwadgv'''
print(a)

Indexing In String:-
It is a process of accessing the elements sequentially of a string.It is of two types:-
1.Positive:-0 to n-1(Left to Right)
2.Negative:-(-1) to -(n-1)(Right to Left)
# In[9]:


a="Lakshita"
print(a[0])
print(a[1]) #It will give out of index error if we print some index bigger than the length of the string

for loop with strings:-
It is used when we don't want to know the actual length of a long string but leaves it for the for loop to calculate and print accordingly.
# In[14]:


a="""He took a sip of the drink.He wasn't sure whether he liked it or not. 
"""
for char in a:
    print(char) #printing the wghole string without using the for loop 
    #prints all the characters one by one in next line

String Slicing:
It is a method to access the elements or parts of a string
Syntax:-string_name[start_value(By Default Zero),End_value(prints one less than it and by default value is last character of the string),step(By default 1)]
The counting in strings starts from zero
# In[19]:


a="Lakshita"
print(a[0:3:1]) #slicing of the string
print(a[:5:])
print(a[0:])
print(len(a)) #prints the length of the string
print(a[2]) #prints value at the specified index
print(a[-1:-5:-1]) #negative index compulsory to give -1 as the step value and prints the result in reverse

Methods for String:-
These methods do not change the original string but make a copy of that string with desired modifications.
1..upper():- Converts the whole string into Uppercase
2..lower():- Converts the whole string into Lowercase
3..strip():- Removes the white spaces before and after the string
4..rstrip():-Removes the characters from the last of any string 
5..replace():-Replaces all occurence of the string with another string
6..split():-Splits the data by the separtor given and splits the data into 2 separate elements of the same list
7..capitalize():-Capitalizes the first letter of the first word and converts rest first letters to lowercase.
8..center():- Aligns the string to the center as per the value given as the parameter,it adds that much spaces to make the string of the specified length.
9..count():- Gives the occurence of the string in a particular string
10..endswith():- Gives True when a string is ending with the string specified as the parameter
11.startswith():- Gives True when a string is starting with the string specified as the parameter
12..find():- Returns the index at which the string is found for the first time and returns -1 if not found
13..index():-Returns the index at which the string is found for the first time and raises error when not found
14..isalnum():- Returns True when the string is a collection of alphabets(A-Z,a-z),numbers or both. But returns false when any other than these are found in the string
15..isaplha():- Returns True when the string contains alphabets only.
16..islower():- Checks the string contains all characters in lower case or not
17..isupper():- Checks the string contains all characters in upper case or not
18..isprintable():- Returns True when a string is printable(i.e. it contains letters, digits, commas, brackets, and question marks.)
19..isspace():-Returns True when the string contains space in between 
20..istitle():-Returns True when every first letter of every word is capitalized
21..swapcase():-changes uppercase to lowercase and vice versa
22..title():- Converts the string into title with first letter of each word capitalized
# In[1]:


a="abcdefg"
print(a.upper()) #uppercase conversion


# In[2]:


b="ABCDEF"
print(b.lower()) #lowercase conversion


# In[3]:


c=" Lakshita "
print(c.strip())


# In[6]:


d="ABCDERFG!@"
print(d.rstrip("!,@")) #multiple characters can be given to remove
#if same character is there many times then by passing it in rstip it will delete all the characters of the same type


# In[8]:


e="ABAAAA"
print(e.replace("A","E")) #Syntax :- replace("string to be replaced","Nwe string to be inserted at that same place")


# In[9]:


f="Lakshita Mukati"
print(f.split(" ")) #returns a list


# In[11]:


g="hey There!"
print(g.capitalize())


# In[16]:


h="Lakshita Mukati"
print(h.center(125))
print(h.center(125,"*")) #prints that pattern for the remaining whole line with the string in the center


# In[18]:


i="hey hi hello hey hi hi "
print(i.count("hi"))


# In[47]:


j="Lakshita Mukati!!!!"
print(j.endswith("!"))
print(j.endswith("aks",0,4)) #search for the string in specified indexes
print(j.startswith("Laksh"))


# In[29]:


k="She is a good girl.She loves to sing a lot."
print(g.find("is")) #returns -1 when string is not found 
#can be used when we are not sure of occurence of the string in our string


# In[30]:


l="ALPHAnumeric3"
print(h.isalnum())


# In[31]:


m="SHXUSHBXJSXHJX"
print(i.isalpha())


# In[45]:


n="kwhedfkuhw"
print(n.islower())
print(n.isupper())


# In[37]:


o="asch \n" # as new line character is not printable it just shifts the cusor to the next line without printing anything
print(o.isprintable())


# In[43]:


p=" "
print(p.isspace())


# In[44]:


q="Lakshita Mukati"
print(q.istitle())


# In[48]:


r="She is a girl.He is a boy"
print(r.swapcase())


# In[49]:


s="ushdcydg iudhbhud shdxbhud"
print(s.title())


# In[ ]:




