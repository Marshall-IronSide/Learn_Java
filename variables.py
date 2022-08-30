"""Nommer une variable : doit commencer par une lettre ou un underscore (_)
                        ne pas conternir de caracteres speciaux
                        ne pas contenir d'espaces
                        utiliser des underscores (_)
                        
    Types standards de donnees : entier  numerique (int)
                                nombre flotant (float)
                                chaine de ccaracteres (str)
                                booleen (bool)"""
                        
age_personne = 22
nom_personne = "IronSide"
prix = 23.9
relancer_partie = True

#afficher type de variable foction type
print(type(age_personne))
print(type(nom_personne))
print(type(prix))
print(type(relancer_partie))

#afficher valeur de variable
print(age_personne)
print(nom_personne)
print(prix)
print(relancer_partie)
print("age de IronSide :", age_personne, "ans")

#formater du texte methode .format
#1ere methode
text = "l'age de IronSide est de {} ans et le prix HT est de {}€"
print(text.format(age_personne, prix))
#2eme methode
print("l'age de IronSide est de {} ans et le prix HT est de {}€".format(age_personne, prix))

#saisie d'information fonction input
nom_joueur = input("Entrez votre nom: ")
print("Bievenue", nom_joueur)

#int(), float(), str(), bool -> "caster" une donnee, la convertir
prixHT = input("entrez un prix:")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT * 20 / 100)
print("PrixTTC =", prixTTC)

valeur_booleen = True
print(valeur_booleen)
valeur_booleen = int(valeur_booleen)
print(valeur_booleen)

valeur_booleen = False
print(valeur_booleen)
valeur_booleen = int(valeur_booleen)
print(valeur_booleen)