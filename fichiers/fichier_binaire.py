import pickle

# Pour enregistrer les donne dans un fichier en format binaire

class Employe:

    def __init__(self, nom, email, tel):
        self._nom = nom
        self._email = email
        self._tel = tel
    
    def afficher(self):
        print("Employe {} : email : {} et tel : {}".format(self._nom,self._email,self._tel))


emp = Employe("salah","salah@gmail.com","0633318619")
# pour ecrire les donnés en binaire format
with open("employes.data","wb") as fic :
    record = pickle.Pickler(fic)
    record.dump(emp)

# pour lire les donnés de binaire format
with open("employes.data","rb") as fic :
    get_record = pickle.Unpickler(fic)
    emp1 = get_record.load()

emp1.afficher()