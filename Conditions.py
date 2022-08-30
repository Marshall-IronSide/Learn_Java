"""Opérateurs de comparaison: == (égale à)
                            != (différent de)
                            < (plus petit que)
                            > (plus grand que)
                            <= (plus petit ou égale à)
                            >= (plus grand ou égale à)
Mots clés des conditions: if/ elif/ else

Conditions multiples:   and (ET)
                        or (OU)
                        in / not in (DANS / PAS DANS)"""
identifiant = "Iron"
mot_de_passe = "Iron24"
print("Interface de conexion")

user_ID = input("Entrez votre identifiant :")
user_password = input("Entrez votre mot de passe :")

if mot_de_passe == user_password:
    print ("Vous êtes connectés, Bienvenue", user_ID)
    
#conditions multiples
identifiant = "IronSide"
mot_de_passe = "13187500"
print("Interface de conexion")

user_ID = input("Entrez votre identifiant :")
user_password = input("Entrez votre mot de passe :")

if mot_de_passe == user_password and identifiant == user_ID:
    print ("Vous êtes connectés, Bienvenue", user_ID)
else:
    print ("Erreur de mot de passe ou d'identifiant ")
    
#in / not in
lettre_hasard = "b"
if lettre_hasard in "aeiouy":
    print("c'est une voyelle" )
if lettre_hasard not in "aeiouy":
    print("c'est une consonne")

#utilisation de mots clés
age = input("entrez votre âge:")
age = int(age)
if age == 18:
    print("Tu viens d'être majeure petit con")
elif age == 22:
    print ("On a le même âge enculé")
else:
    print("tu as", age, "ans mon gars")
    
#conditions avec valeurs booléenes
jeu_lance = True
if jeu_lance:
    print("le jeu est en marche")
else:
    print("Le jeu n'est pas en marche")
    
jeu_nouveau = False
if jeu_nouveau:
    print("le jeu est en marche")
else:
    print("Le jeu n'est pas en marche")
    
jeu_renouveau = False
if not jeu_renouveau:
    print("le jeu est en marche")
    
#astuce -------> age > 0 et age <= 100 --> 0 < age <= 100
age = input("Quel âge as-tu ?:")
age = int(age)
if 0 < age <= 22:
    print("xlu petit frère")
else:
    print("T'es vieux bro")