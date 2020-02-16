

class Personne :

    ville_actu = "Marrakech"

    # Cnostructeur
    def __init__(self,p_name="",p_sexe="",p_age=""):
        self.name = p_name
        self.sexe = p_sexe
        self.age = p_age
        print("Object crée ......... ")

    def parler(self,message):# Methode Standard , il faut instansier un objet du class personne pour avoir accéder à cette methode
        print(message)
    
    def changerVille(cls,message):# Methode de class
        Personne.ville_actu = message
    
    changerVille = classmethod(changerVille)

    def descVille():# Methode static
        print("static methode")
    
    descVille = staticmethod(descVille)






# Maintenant on est pas sur la class personne

p1 = Personne("salah","H",25)
print("Personne aec le nom {} et le genre {} et age {}".format(p1.name,p1.sexe,p1.age))

Personne.descVille()
print(Personne.ville_actu)
p1.changerVille("Tanger")
print(Personne.ville_actu)
p1.parler("see hey")





