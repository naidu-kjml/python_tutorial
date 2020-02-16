
dico = {"chat":"miaw","chien":"how","chevre":"maaa"}

print(dico["chien"])

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