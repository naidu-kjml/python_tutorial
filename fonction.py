# Les Fonctions on Python

def bjr():
    print("Bonjour ;)")

bjr()

def nameEmp():
    return "salah eddine chehbi"

print(nameEmp())

#  avec des parametres optionnel
def descEmp(name_emp="said", age_emp=20) : 
    return "Employe name est {} avec l\'age {}".format(name_emp,age_emp)

print(descEmp("salah eddine chehbi"))
print(descEmp())
print(descEmp("salah eddine chehbi",26))

#sur ces exemple on a garder le meme ordre pour insertion des variables
def desc(name_emp="saad",fonction_emp="khabaz",age_emp=25):
    return " Employe {} est {} ans occupe le poste de {}".format(name_emp,age_emp,fonction_emp)

print(desc())
print(desc("salah Eddine"))
print(desc("salah Eddine",45))
print(desc("salah Eddine",age_emp=35))
print(desc("salah Eddine","Directeur",78))

# pour passer plusieurs variable 

def fct(*list_var):
    for var in list_var :
        print(var)

fct("said")
fct("said","berrada","directeur",63)

# lambda function 
prix_tcc = lambda prix_uni,qtt_pro : (prix_uni * qtt_pro) + ((prix_uni * qtt_pro) * 0.20)

print(prix_tcc(10,2))

#def lambdaa :(prix_uni * qtt_pro) + ((prix_uni * qtt_pro) * 0.20)
