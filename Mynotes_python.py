#!/usr/bin/env python
# coding: utf-8

# ## Python

# In[ ]:


#pip-Preferred Installer Program(install and manages python packages)
pip install jupyter


# In[ ]:


python -m noteboook #opening jupyter notebook in chrome


# In[ ]:


#interpreted, object-priented, high level language
invented by Guido Van Rossum


# In[ ]:


##python interpreter
print("which will convert our code in binary form")
##Integrated Development Environment(Text editor)
print("place where we will write our code,run and debug\n"
"ex-Pycharm,IDLE,jupyter notebook")


# ## Features of python

# In[6]:


print("simple and easy to learn\n"
"free and open source\n"
"high level language\n"
"GUI programming support\n"
"interactive and interpreted\n"
"broad standard library(for ML, use of packages)")


# ## limitations of python

# In[7]:


print("slower than C/C++ due to interpreted language\n"
     "lacks true multiprocessor support\n"
     "not for developing games\n"
     "parallel processing not elegant")


# ## Applications

# # **network programming**
# 
# *data analysis*
# * robotics
# * data visualization
# * ML and AI
# * game development

# In[1]:


#python has two modes
#script(.py)
#interactive(shell)


# ## 33 Keywords in python
# """False, class, finally, is, return, none, continue,
# 
# for, lambda, try, True, def, from, nonlocal, while,
# 
# and, del, global, not, with, as, elif, if, or, yield,
# 
# assert, else, import, pass, break, except, in, raise
# """

# ## Basics

# In[23]:


# "#"-comments(non-executable statements)
print(4**2)
a="hello"
z=True
print(type(a))
print(type(z))
print(4+4)
print("hello"+" mam")
#("hello"+4)-error
True+False
#str()-convert the variables to strings
#float()-convert the variables to floats
print(10/3) #float values
print(10//3) #int values
_+1 # _ indicates previous output
print('Nvin\'s laptop') #\ ignores the special meaning of the quotes
print(r"\naviin") #r-raw string
print(bin(25),hex(25))
print(0b1001)


# In[2]:


#Actual Syntax of the print() function
print("hello",sep="$",end="1\n")


# In[ ]:


#Indentation
whitespace at the beginning of the line.


# ## Bitwise operators

# In[32]:


a=10 #0000 1010
b=4 #0000 0100
print(a&b) #bitwise AND (returns 1 if both inputs are 1's)
print(a|b) #bitwise OR
print(~a) #bitwise NOT(2 COMPLEMENT)
print(a^b) #bitwise XOR (returns 1 if both inputs are different)
print(a<<2) #bitwise left shift
print(a>>2) #bitwise right shift


# ## Functions and Methods

# In[1]:


#functions- piece of reusable code, solves particular task, call function instead of writing code
#type(), print()
print(len("hello")) #prints the length of the string
print(round(12.5,-1))
print(complex(4,5))
a=10
print(id(a)) #address/memory location of the variable a
#methods- call functions specific to python objects(functions that belong to objects)
#str----capitalize(), replace(), upper()
#float--bit_length(), conjugate()
#list--index(), count()


# In[1]:


#Extraction subsets of strings by using the slice operator[]
name="Pakhi Changia"
print(name[0]) #indexing starts with zero
print(name[-1])
print(name[5:10]) #[start:end] or [inclusive:exclusive]
print("My name is ",name)
#strings in python are not mutable i.e. name[3]=k gives the error
name=name.replace("Changia","Goyal")
print(name)
bool()


# ## Objects/Data Structures

# ### lists

# In[93]:


#python lists- mutable,or changeable and ordered sequence,comma separated values, each element is called an item
lst=[] #slice operator
# we can create a list by using an inbuilt function i.e. list()
list1=[1,2,3,"a","b","c"] #any data type
list3=[4,5,6]
list4=[6,7,8]
print(list1)
print(type(list1))
list2=[[1,2,3],["a","b","c"]]
print(list2)
print(list2[1]) 
print(list2[0:1])
print(list1[1]+list1[2]) #calculations element to element calculations
print(list3+list4) #concatenate
list2[0:1]=[[0,1,2]] #change list items
print(list2)
print(list2+["A","B","C"]) #adding list items
print(list2+[["A","B","C"]])
del(list1[2]) #deleting list items
print(list1)
print(type([]))
print(len(list2))
print(list1[:])


# In[92]:


#functions and methods in lists
list1=[1,2,3,"a","b","c"]
list2=[1,3,4,5,2,2,6]
list1.append("d") #add at the end of the list
print(list1)
list1.append([4,5]) #nested list
print(list1)
list1.extend([4,5])
print(list1)
list1.insert(3,4) #insert at index number 3, the value 4
print(list1)
print(list1.index("a")) #tells the index number of the char "a". we can also state first and last value index.
print(list2.count(2)) #occurrence of the value 2
print(list1)
print("12",list1.pop()) #extracts the last value by default and then removes that value
print(list1)
print(list1.pop(2)) #extracts the value at index number 2
print(min(list2)) #minimum value of the list
print(sum(list2)) #sum of the list
list2.sort() #sorting the values
print(list2)
print(list(range(2,10,2))) #range(start_value,end_value,difference)
list2*2


# In[28]:


#Reference based copy
x=[1,2,3]
y=x
y[1]=4
print(y)
print(x) 
#Explicit copy
a=[1,2,3]
b=list(a) # we can also use b=a[:]
b[1]=4
print(b)
print(a)


# ### Tuples

# In[2]:


tup=() 
#not mutable
tup1=(1,2,3,4,3)
print(tup1)
#not mutable i.e tup[1]=3 gives the error, I can replace whole tuple.
#iteration is faster in tuples than in list
print(tup1.count(3)) #counts the occurrence of value 3
print(tup1.index(2)) #tells the index number of value 2


# ### Sets

# In[99]:


S={} #collection of unordered unique elements, iterable, mutable
#we can create a set by using an inbuilt function set()
S1={1,2,3,4}
S2={4,6,8}
#sets never follow a sequence, indexing not there S[2]=3 gives the error
#elements are not mutable but the whole set itself is mutable
#based on a data structure known as hash table
#In computing, a hash table (hash map) is a data structure that implements an associative array abstract data type, a structure that can map keys to values. 
#no indexing
S1.add(5)
print(S1)
print(S2.difference(S1)) #extract the different elements in S2 from S1
S2.difference_update(S1) #updating the values in S2
print(S2)
S2={4,6,8}
print(S2.intersection(S1)) #extract the common elements in S2 from S1
S2.intersection_update(S1) #updating the values in S2
print(S2)
print(sum(S1))
print(min(S1))
S3={1,2,3,4,1}
print(S3)


# ### Dictionaries

# In[1]:


data={1:"pakhi",2:"parul",3:"kishna"} #stores data in key-value pairs
#unordered, changeable, indexed
print(data[1]) #here indexing includes keys
data[2]="rupal" #changing
data[4]="sahil" #adding  
print(data)
del(data[4]) #deleting
print(data)
print(data.keys()) #printing keys and values
print(data.values())
print(data.get(4,"not found"))


# In[5]:


data={1:"pakhi",2:"rupal",3:"kishna"}
# for loop for printing keys & values
for x in data:
    print(x)
for x in data.values():
    print(x)
for x in data.items():
    print(x)
#nested dictionary
car1_model={"merecedes":1960}
car2_model={"audi":1970}
car_type={"car1":car1_model,"car2":car2_model}
print(car_type)
print(type(car_type))
print(car_type["car1"]["merecedes"])


# In[6]:


name1="Pakhichangia2"
name2="PAKHI"
name3=" "
name4=""
print(name1.isalpha()) #spaces are not allowed
print(name1.isalnum()) #spaces are not allowed
print(name2.isalnum())
print(name1.istitle()) #if the string contains title wrds i.e.  only first alphabet capital, if there is another alphabet capital, returns false
print(name1.isdigit()) #if all the numbers #spaces are not allowed
print(name2.isupper()) #if all the chars are upper
print(name1.islower())
print(name3.isspace())#if all the chars have space
print(name4.isspace())
print(name1.startswith('p')) #case sensitive


# ## Boolean relational and logical operators

# In[76]:


print(True-False) #true=1, false=0
print(True and False)
print(True or False)
print(True and True)
print(True or True)
name1="pakhi"
name2="changia"
print(name1.isdigit() and name2.isalpha())

