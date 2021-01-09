""" Eisen V:
De applicatie blijft aanstaan tot er iemand heeft gewonnen met 2 punten
De applicatie is werkend en het spel kan gespeeld worden
De applicatie heeft 2 functies
De applicatie wordt optijd opgeleverd
"""
from array import *
import random

# 1d array [rondex, rondex, rondex, rondex]
ronde = [0]

# 2d array [[playernaam, playernaam, playernaam],[punten p1, punten p2, punten p3]]
namePlayArr = [["a", "b", "c"],[0, 0, 0]]

# de waarde vaan sps
steen = 1
papier = 2
schaar = 3

# een functie die random steen, papier of schaar genereerd als de gebruiker tegen de pc speelt
# def pckeuze():
#     pcrand = random.randint(1, 3) 
#     if pcrand == 1:
#         return pcrand
#     if pcrand == 2:
#         print("De pc kiest papier")
#         return pcrand  
#     if pcrand == 3:
#         print("De pc kiest schaar")
#         return pcrand  

# een functie die weegt wie wint. Steen papier of schaar.
def weegschaal():
    # gelijkspel
    if pvc == pckeuze:
      print("\ngelijkspel")
    elif pvc == 1:
        if pckeuze == 3:
            print ("\Gefeliciteerd jij wint")
        else:
            print("Helaas, je hebt verloren")
    elif pvc == 2:
        if pckeuze == 1:
            print("Gefeliciteerd jij wint")
        else:
            print("Helaas, je hebt verloren")
    elif pvc == 3:
        if pckeuze == 2:
            print("Gefeliciteerd jij wint")
        else:
            print("Helaas, je hebt verloren")
    else:
        print("De door jou genomen keuzen wordt niet herkend ")

    
         
# een welkom menu met opties zoals 1p, 2p, 3p of stoppen(exit)
print("Welkom Wat is je naam?")
name1 = input("mijn naam is: ")

print ("\nWelkom {} bij steen papier schaar! Maak een keuze door middel van een cijfer te antwoorden.\n ".format(name1))
namePlayArr[0] = name1 #de naam wordt geplaats in de array

# een loop zodat het spel nooit zich zelf afsluit tenzij de gebruiker daar voor kiest
keuzeMenu = True
while keuzeMenu:
    keuze = int(input("\nmaak een keuze {}.\n1. Player vs pc\n2. Player vs player\n3. 3 Player game\n4. Exit\n\r".format(name1)))
    if keuze == 1:   
        print(namePlayArr[0],[0])
        # een loop voor de 1p spel
        eenPlayerGame =  True
        while eenPlayerGame: # een loop zodat het spel aanblijft tot iemand heeft gewonnen
            pvc = int(input("\n{} maak een keuze\n1. steen\n2. papier\n3. schaar\n\n".format(name1)))
            pckeuze = random.randint(1, 3) 
            if pckeuze == 1:
                print("De pc kiest steen")
            if pckeuze == 2:
                print("De pc kiest papier")
            if pckeuze == 3:
                print("De pc kiest schaar")
            weegschaal()

    elif keuze == 2:
        # een loop voor de 2p spel
        tweePlayerGame =  True
        while tweePlayerGame: # een loop zodat het spel aanblijft tot iemand heeft gewonnen
            print("Welkom player 2 Wat is je naam?")
            name2 = input("mijn naam is: ")
            namePlayArr[1] = name2 #de naam wordt geplaats in de array

    elif keuze == 3:
        # een loop voor de 3p spel
        driePlayerGame = True
        print("3 player game is op dit moment onder contstructie.")

    elif keuze == 4:
        print("\ntot de volgende keer {}!".format(name1))
        keuzeMenu = False

    else:
        print("\nDe door jou genomen keuzen wordt niet herkend {}. Maak keuze uit 1, 2, 3 of 4\n".format(name1))
