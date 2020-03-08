"""
Python dictionary is a container of the unordered set of objects like lists. 
The objects are surrounded by curly braces { }. 
The items in a dictionary are a comma-separated list of key:value pairs where keys and values are Python data type.

Each object or value accessed by key and keys are unique in the dictionary. 
As keys are used for indexing, they must be the immutable type (string, number, or tuple). 
You can create an empty dictionary using empty curly braces.
"""

#Empty dictionary
new_dict = dict()
new_dict = {}
print(new_dict)
#Dictionary with key-vlaue
color = {"col1" : "Red", "col2" : "Green", "col3" : "Orange" }

dico = {"chat":"miaw","chien":"how","chevre":"maaa"}
print(dico["chien"])

#Accessing value using get() method
print(dico.get("chat"))
#dict.keys()
for k in dico.keys():
    print(k)
#dict.values()
for v in dico.values():
    print(v)
#dict.items()
for k,v in dico.items():
    print("Key : {} a une valeur : {}".format(k,v))

#dict.copy()
dico2 = dico.copy()
#del dict
del dico['chien']
#dict.pop()
valeur_supprimer = dico.pop("chat")

print(dico)
print(valeur_supprimer)

#Sort a Python dictionary by key

color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))

#Concatenate two Python dictionaries into a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3):
     dic4.update(d)
print(dic4)