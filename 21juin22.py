#!/usr/bin/env python
# coding: utf-8

# Programme de calcul du plus petit élément : 

# In[3]:


smallest = None
list = [104, 8, 23, 5, 7, 8, 17, 4837, 23, 1213, 3455, 35663, 2134]
for elt in list:
    if smallest is None or elt < smallest:
        smallest = elt
print(smallest)


# Différence entre is (égalité sur la valeur et le type) et == (égalité sur la valeur)

# In[11]:


a = 0
b = 0.0
print(a is b)
print(a == b)
print(a is not b)


# Loop on strings

# In[18]:


fruit = 'banana'
for loop in range(len(fruit)):
    print(fruit[loop])
    
fruit = 'apple'
for letter in fruit:
    print(letter)
    
sentence = "Bonjour, je m'appelle Caroline et je suis actuellement en formation au CCI"
count = 0
for letter in sentence:
    count += 1
print(f"there are {count} letters in the sentence: {sentence}")


# Méthod on strings. slice, concatenation with +, < for alphabetical order, dir(str) : liste de tous les méthodes sur les objets String. Les méthodes sur les strings ne changent jamais le string d'origine. 
# .lower()
# .upper()
# .capitalize()
# .find('string', index1, index2) entre index1 et index2
# .replace('name', 'name2')
# .lstrip() enlève les espaces à gauche
# .rstrip() enlève les espaces à droite
# .strip() enlève les espaces à droites et à gauche
# .startswith('M')
# 

# In[39]:


name = "Monty Python"
print(name[0:4])
print(name[6:7])
print(name[6:20])
print(name[:2])
print(name[8:])
print(name[:])
print('caro'>'MS')
a = name.lower()
print(a)
a = name.upper()
print(a)
a = name.capitalize()
print(a)
type(a)
print(dir(str))
#help(str)

a= name.find('ty')
print(a)
a = name.find('caro')
print(a)
a = name.replace('thon', 'round')
print(a)
print(name.startswith('M'))


# In[50]:


message = 'I have an email adress that is czumbiehlfaure@hotmail.fr since 2005'
index = int(message.find('@'))
index1 = int(message.find(' ', 0, index))
print(index1)
index2 = int(message.find(' ', index))+1
print(index2)
email = message[index1: index2]
print(email)


# Opening files : 
# fhandle = open('filename.txt', 'r')     filename is a string, r is the mode. If reading, it doesn't harm the file, you can read it over and over. If writing mode, if there is already data in the file, it truncates it and writes something, we are not really gonna write file, we are mostly gonna read them --> open pass it in a file... it gives you back this file handle. Open() allows you to get into the file. 
# 
# A noter que dans un fichier .txt, quand on l'importe .open(), on obtient une séquence de strings qui sont déterminés par le passage à la ligne \n (servent de séparateur entre les différents éléments string que l'on importe). Each list item is a string.

# In[76]:


fhandle = open('data.txt','r')
print(fhandle)
number = 0
for listItem in fhandle:
    number += 1
    print("listItem:", number, "- ", listItem)


# check if file name is correct
# quit() to end the program

# In[84]:


fileName = input('what is your file name?')
try :
    filehand = open(fileName)

except:
    print("file can not be opened:", fileName)
    quit()
    


# In[ ]:




