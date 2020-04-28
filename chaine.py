

my_chaine = "bonjour tout le monde"

#  my_chaine = my_chaine.upper()

#  my_chaine = my_chaine.lower()

#  my_chaine = my_chaine.strip() # pour enlever tout les espaces

#  my_chaine = my_chaine.capitalize() # il permet de metre le premier litre du phrase en majuscule

#  my_chaine = my_chaine.title() # il metre tout les premier litres des mots en majuscule

#  my_chaine = my_chaine.center(50) # str.center(<largeur>,<caractere_remlisage>)

#  my_chaine = my_chaine.center(50,"-") il permet de deplacer la chaine de caracteres de 50 caracteres a droit et remplcer espace avec --

#  my_chaine = my_chaine.replace("bonjour","bonsoir") # str.replace(<old_value>,<new_value>,<start>,<end>) pour changer une valeur 

#  my_chaine = my_chaine.split(" ") 

# index = my_chaine.find("tout") # str.find(<chaine de caractere>,<start>,<end>) il nous rendre index de cette chaine sur notre variable et nous rendre -11 si il n'a rien trouver 

# str.index(<chaine de caractere>,<start>,<end>) la meme principe que find() ms cette fois il lence une exception ValueError si n'a rien trouver


try:
    index = my_chaine.index("tout")
    print(index)
except ValueError:
    print("NotExist")

# my_chaine.islower() # verifier si tout les caractere son miniscule
# my_chaine.isupper() # verifier si tout les caractere son majuscule


if my_chaine.islower() :
    print("Miniscule")
else:
    print("Majuscule")

if "tout" in my_chaine :
    print("Trouvé")
else:
    print("Nom Trouvé")
