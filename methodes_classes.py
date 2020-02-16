
#class Personne

class Personne :

    entreprise_actuell = "KS-Events" # varialbe de class

    def __init__(self, p_nom,p_age,p_sexe):
        self.nom = p_nom
        self.age = p_age
        self.sexe = p_sexe
    
    def parler(self,message):# methose standart pour acceder a cette class il faut instansier une unstance de cette class
        print("{} a dit {}".format(self.nom,message))

    def changeEntreprise(cls,nouvelle_entreprise):# methoode de class on peut l'appeler son avoir objet instansier
        Personne.entreprise_actuell = nouvelle_entreprise
    
    changeEntreprise = classmethod(changeEntreprise)

    def definition():
        print("Hello from this class, i am a static methode you can call were ever you are with this class.methodeName")
    
    definition = staticmethod(definition)


#programme principale

p1 = Personne("Salah Eddine",26,"M")

p1.parler("Bonjour")

print(Personne.entreprise_actuell)
Personne.changeEntreprise("Mission Conseil")
print(Personne.entreprise_actuell)
Personne.definition()