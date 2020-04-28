from classes.Employe import Employe


class Commercial(Employe):

    def __init__(self,_id,_nom,_sexe,_age,_lamarge):
        Employe.__init__(self,_id,_nom,_sexe,_age)
        self.lamarge = _lamarge
    
    def affiherComm(self):
        print("L'employé {} de sexe {} et d'age {} et un id {} a une marge de {}".format(self.nom,self.sexe,self.age,self.id,self.lamarge))

    def compare(self,other):
        if self.lamarge == other.lamarge :
            return True
        else :
            return False
