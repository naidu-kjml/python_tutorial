


prix_unitaire = float(input("Entrer le prix du produit : \n"))
qtt_produit = int(input("Entrer quantite : \n"))

prix_ht = prix_unitaire * qtt_produit

print("prix hors taxe est : {}".format(prix_ht))

prix_tcc = prix_ht + (prix_ht * 0.20)

print("prix avec taxe est : {}".format(prix_tcc))
