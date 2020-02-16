
#Class Mére
class Employe :
    
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age
    
    def afficher(self):
        print("Employe {} est {} ans".format(self._nom,self._age))


#Class Fille
class Comptable(Employe):

    def __init__(self, nom, age, fonction):
        Employe.__init__(self,nom,age)
        self._fonction = fonction
    


#Programme principale

c1 = Comptable("salah",26,"comp")
c1.afficher()
