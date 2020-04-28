from classes.Employe import Employe



class Comptable(Employe):

    def __init__(self,_id,_nom,_sexe,_age,_salaire):
        Employe.__init__(self,_id,_nom,_sexe,_age)
        self.salaire = _salaire

    def AficherComp(self):
        print("L'employé {} de sexe {} et d'age {} et un id {} au salaire de {}".format(self.nom,self.sexe,self.age,self.id,self.salaire))
