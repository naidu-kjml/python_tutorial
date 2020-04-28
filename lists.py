
# Création d'une liste
my_list1 = [5, 12, 13, 14] # the list contains all integer values
my_list2 = ['red', 'blue', 'black', 'white'] # the list contains all string
my_list3 = ['red', 12, 112.12] # the list contains a string, an integer and
#print(my_list2)

l1 = list()
l2 = []

l3 = [1] * 10
#print(l3)

l4 = ["salah"] * 5
#print(l4)

l5 = range(20) #donné des valeurs entre 0 est 20
"""
for v in l5:
    print(l5[v])
"""

l6 = ["said","salah","safaa","salwa","saad","samira","samir","salma","saif","samia"]
print(l6[3:]) # nous rendre les elements qui se trouve aprés index 3 de la liste, 3 est parmie les idices 
print(l6[:3]) # nous rendre les elements qui se trouve avans index 3 de la liste, on compte pas indice 3
print(l6[2:4]) # nous rendre les elements qui se trouve entre index 2 et 4 
"""
if "said" in l6 :
    print("yes")
else:
    pass
"""
# l6.append("sahar") # inseré element a la fin du liste
# l6.insert(2,"sahar") # inseré element à l'indice  2 du liste
# l6.remove("salwa") #supprimer par element
# del l6[2] # supprimer par index
# l6.index("salah")
# l6.sort() trie 
# l6.reverse()
# l6.count("salah") # count le nbr de fois un element exist dans cette liste

"""
my_list = ["bonjour","tout","le","monde"]
my_text = " ".join(my_list)
my_text = "-".join(my_list)
print(my_text)
"""

"""
# cette copier quand on ajoute un element a la deuxieme liste il ajoute automatiquement a la premiere liste
# donc c'est pas pratique par ce que il faut quand garde notre premiere liste libre 
#pour cela on travaille avec package copy   
""" 
l7 = ["said","salah","safaa"]
l8 = l7
#print(l7)
#print(l8)
l8.append("salma")
#print(l7)
#print(l8)
import copy
l9 = ["said","salah","safaa"]
l10 = copy.deepcopy(l9)
#print(l9)
#print(l10)
l10.append("salma")
#print(l9)
#print(l10)

#pour faire la concatunation entre les listes
l11 = ["said","salah","safaa"]
l12 = ["salma","samir"]
l11 += l12
#l11 = l11 + l12
#print(l11)

"""
for k,v in enumerate(l11):
    print("indice d'element {} est -> {}".format(v,k))
"""
l15 = [[1,5],[7,5],[3,6]]
#print(l15[0][1])
"""
for r in l15:
    print(r)
    for t in r:
        print(t)
"""
arr = [5,9,3,1,5]
"""
for i in range(5):
    print(arr[i])

for n in arr:
    print(n)
"""



