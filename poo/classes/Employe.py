class Employe:

    def __init__(self,_id,_nom,_sexe,_age):
        self.id = _id
        self.nom = _nom
        self.sexe = _sexe
        self.age = _age
    
    def afficher(self):
        print("L'employé {} de sexe {} et de fonction {} et un id {}".format(self.nom,self.sexe,self.age,self.id))


    def __str__(self):
        print("L'employé {} de sexe {} et de fonction {} et un id {}".format(self.nom,self.sexe,self.age,self.id))


    
