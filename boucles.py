compteur = 0
while compteur < 7:
    print("Ironside")
    compteur += 1
    
print("fin de la boucle")

#boucle booleene
"""Boucles: While /for
    Mots clés: Break (sort de la boucle)/ continue (revient au début de la boucle)
"""
#while
jeu_lance = True
while jeu_lance:
    choix_menue = input(">")
    if choix_menue == "again":
        continue;
    elif choix_menue == "quit":
        jeu_lance = False
    elif choix_menue == "hello":
        print("Bonjour :) !")
    else:
        print("commande introuvable")
print("A bientôt ....")

#for
sentence = "Hello everyone :)!"
for letter in sentence:
    print(letter)
