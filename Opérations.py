"""Opérateurs en pyhon: + (addition)
                        -(soustraction)
                        *(multiplication)
                        /(division)
                        % (modulo: reste d'une division euclidienne)
                        
        variable = variable + x
     même chose si on écrit -> variable += x 
     variable = variable - x
     même chose si on écrit -> variable -= x
     variable = variable * x
     même chose si on écrit -> variable *= x
"""
                        
calcul = 5 / 2
calcul = float(calcul)
Reste  = 5 % 2
Reste = int(Reste)
print("Résultat =", calcul, "Reste = ", Reste)

#Modification de valeur

niveau_personnage = input("niveau de départ :")
niveau_personnage = int(niveau_personnage) 
print("Niveau de départ du personage =", niveau_personnage)
niveau_personnage = niveau_personnage + 2
print("Combat réussit, tu gagnes de 2 niveau ! =", niveau_personnage)
niveau_personnage += 5
print("deuxième combat réussit, tu gagnes de 5 niveau ! =", niveau_personnage)