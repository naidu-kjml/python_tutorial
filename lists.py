
# Création d'une liste

l1 = list()
l2 = []
l3 = [1] * 10
l4 = ["salah"] * 5
#print(l4)
l5 = range(20) #donné des valeurs entre 0 est 20
"""
for v in l5:
    print(v)
"""
l6 = ["said","salah","safaa","salwa","saad","samira","samir"]
# print(l6[3:]) # nous rendre les elements qui se trouve aprés index 3 de la liste  
# print(l6[:3]) # nous rendre les elements qui se trouve avans index 3 de la liste  
# print(l6[2:4]) # nous rendre les elements qui se trouve entre index 2 et 4 
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
# # donc c'est pas pratique par e que il faut quand garde otre premiere liste libre 
# #pour cela on travaille avec package copy    
l7 = ["said","salah","safaa"]
l8 = l7
print(l7)
print(l8)
l8.append("salma")
print(l7)
print(l8)
import copy
l9 = ["said","salah","safaa"]
l10 = copy.deepcopy(l9)
print(l9)
print(l10)
l10.append("salma")
print(l9)
print(l10)
"""
#pour faire la concatunation entre les listes
l11 = ["said","salah","safaa"]
l12 = ["salma","samir"]
l11 += l12
#l11 = l11 + l12
print(l11)

for k,v in enumerate(l11):
    print("indice d'element {} est -> {}".format(v,k))