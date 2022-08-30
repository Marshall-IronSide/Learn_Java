"""fonctions: print(), input()
                type(), int(), float, str(), bool"""
                
age = input("How old are u ? :")
age = int(age)
print("U are {} years old".format(age))

#définir ma propre fonction
def say_hello():
    print("hello motherfucker :) !")

say_hello()

def say(person_name, message_person):
    print("{} : {}".format(person_name, message_person))
    
say("Iron", "evening mothefucker")
say("Jason", "who the fuck u calling mothefucker ?")
say("Iron", "U bitch")
say("jason", "fuck u !")
say("Iron", "fuck u !")

def say_new(person_name ="Iron", message_person ="Why the fuck i can't talk to here ?"):
    print("{} : {}".format(person_name, message_person))
    
say_new()

#faire une liste d'items
def show_invetory(*list_items):
    for item in list_items:
        print(item)
show_invetory("épée")
show_invetory("épée", "arrow", "mana","dragon blood")

#fonction qui retourne une valeur
def calculer_somme(nombre1, nombre2):
    resultat = nombre1 + nombre2 * nombre2
    return resultat
print(calculer_somme(5, 16))

def nouvea_calcul(nb1, nb2):
    return nb1 * nb2 - nb2
print(nouvea_calcul(16, 22))