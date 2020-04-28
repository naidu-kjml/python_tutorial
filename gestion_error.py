#pour gerer les exeptions

#value exception error 
"""
age_util = input("entrer votre age ici : \n")
try:
    age_util = int(age_util)
    print("votre age est {}".format(age_util))
except ValueError:
    print("entrer un nombre valide")
"""
#value exception error 

try:
    nbr_util = input("entrer nbr util ici : \n")
    nbr_depa = input("entrer nbr depa ici : \n")
    nbr_util = int(nbr_util)
    nbr_depa = int(nbr_depa)
    nbr = nbr_util / nbr_depa
    print("nbr par departement est {}".format(nbr))
except ZeroDivisionError:
    print("impossible de deviser sur 0")
except ValueError:
    print("entrer un nombre valide")
