#!/usr/bin/env python
# coding: utf-8

# # Dictionaries In Python:-
# These are the ordered collection of data items.They store multiple items in a single variable.Dictionary items are key-value
# pairs that separated by commas and enclosed within curly brackets{}.

# In[10]:


dict={
    "Aap":"You",
    "Aur":"And",
    "Aapka":"Your",
    "Bhai":"Brother"
}
print(dict)
print(dict["Aur"])
print(dict.get("Bhai")) #get()is used for acessing a single value by giving key.It also gives none when that key is not there.
#It doesn't give the valueerror.
print(dict.get("Lakshita"))
print(dict.values()) #gives values of the dictionary
print(dict.keys()) #gives keys of the dictionary
print(dict.items()) #gives the key value pair


# # Dictionary Methods:-
# 1.dict.update():-updates the value of the key provided to it if the item already exsists in the dictionary,else it creates a 
# new key-value pair.
# 2.dict.clear():-Used to remove all the items from the list.
# 3.dict.pop(key):-Removes the elements whose key is being passed.
# 4.dict.popitem():-Removes the last item pair.
# 5.del :-a keyword used to remove a dictionary item, if given or otherwise the complete dictionary

# In[14]:


dict={1:"A",2:"B",3:"C",4:"D"}
d2={5:"E",6:"g"}
print(d2)
d2.update({6:"F",7:"G"})
print(d2)
d2.clear()
print(d2)
d3={1:"Mango",2:"Apple",3:"Strawberry",4:"Chocolate",5:"Bubblegum"}
print(d3)
d3.pop(5)
print(d3)
d3.popitem()
print(d3)


# In[17]:


d4={"name":"Lakshita","Gender":"Female","City":"Indore"}
del d4["Gender"]
print(d4)
#del d4
#print(d4) deletes the whole dictionary

