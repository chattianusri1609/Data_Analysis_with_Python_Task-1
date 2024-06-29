#!/usr/bin/env python
# coding: utf-8

# In[9]:


#creating a list
my_list=[1,2,3,4,5,6,7,8,9]
print("Original list:", my_list)
#Adding an element to the list
my_list.append(10)
print("List after adding an element:", my_list)
#Removing an element from the list
my_list.remove(5)
print("List after removing an element:", my_list)
#Modifying an element in the list
my_list[1]=200
print("List after modifying an element:", my_list)
print("My updated List:",my_list)


# In[10]:


#Creating a dictionary
my_dict={'name':'Avi','age':'20','city':'Hyderabad'}
print("Original dictionary:", my_dict)
#Adding an element to the dictionary
my_dict['gender']='Male'
print("Dictionary after adding a key-value pair:", my_dict)
#Removing an element from the dictionary
my_dict['age']
print("Dictionary after removing a key-value pair:", my_dict)
#Modifying an element in the dictionary
my_dict['city']='Delhi'
print("Dictionary after modifying a value:", my_dict)
print("My updated dict:",my_dict)



# In[11]:


#Creating a set
my_set={1,2,3,4,5}
print("Original set:", my_set)
#Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)
#Removing an element from the set
my_set.remove(4)
print("Set after removing an element:", my_set)
#Modifying an element in the set
my_set.discard(3)
my_set.add(9)
print("My updated set:",my_set)


# In[ ]:




