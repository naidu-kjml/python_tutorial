
class Personne :

    def __init__(self, nom, age):
        print("Creation d'un objet ...")
        self._nom = nom
        self._age = age
    
    # si on a pas un controlle sur les methodes getters et seetters donc c'est unitile de l'utilisé
    def _getage(self):
    try:
        return self._age
    except AttributeError :
        print("l'age n'existe pas")
    
    def _setage(self, nouvelle_age):
        if nouvelle_age < 0 :
            self._age = 0
        else :
            self._age = nouvelle_age
    
    # properties(<getter>,<setter>,<deleter>,<helper>)

    age = property(_getage, _setage)