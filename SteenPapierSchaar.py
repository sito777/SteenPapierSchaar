""" Eisen V:
De applicatie blijft aanstaan tot er iemand heeft gewonnen met 2 punten
De applicatie is werkend en het spel kan gespeeld worden
"""
from array import *
import random
import os

# 1d array [rondex, rondex, rondex, rondex]
ronde = [0]

# 2d array [[playernaam, playernaam, playernaam],[punten p1, punten p2, punten p3]]
namePlayArr = [[],[]]

# de waarde vaan sps
steen = 1
papier = 2
schaar = 3

# een functie die random steen, papier of schaar genereerd als de gebruiker tegen de pc speelt
# def pckeuze():
#     pcrand = random.randint(1, 3) 
#     if pcrand == 1:
#         return pckeuze
#     if pcrand == 2:
#         print("De pc kiest papier")
#         return pckeuze  
#     if pcrand == 3:
#         print("De pc kiest schaar")
#         return pckeuze  

#terminal wordt schoon gemaakt zodat de spelers niet kunnen afkijken
def clear(): 
    os.system('clear')

# een functie die weegt wie wint. Steen papier of schaar.
def weegschaal():
    # gelijkspel
    if pvc == pckeuze: #pvc(Player VS Computer) is player 1 
        if pvc == 1:
          print("Jij kiest steen")
        elif pvc == 2:
            print("Jij kiest papier")
        elif pvc == 3:
            print("Jij kiest schaar")
        print("Het is gelijkspel")
    elif pvc == 1:
        print("Jij kiest steen")
        if pckeuze == 3:
            print ("Gefeliciteerd jij wint")
        else:
            print("Helaas, je hebt verloren")
    elif pvc == 2:
        print("Jij kiest papier")
        if pckeuze == 1:
            print("Gefeliciteerd jij wint")
        else:
            print("Helaas, je hebt verloren")
    elif pvc == 3:
        print("Jij kiest schaar")
        if pckeuze == 2:
            print("Gefeliciteerd jij wint")
        else:
            print("Helaas, je hebt verloren")
    else:
        print("De door jou genomen keuzen wordt niet herkend ")

# een functie die weegt wie wint. Steen papier of schaar.
def weegschaal2P():
    # gelijkspel
    if pvc == pvp: #pvc(Player VS Computer) is player 1. pvp(Player VS Player) is player 2
        if pvc == 1:
          print("Jij kiest steen")
        elif pvc == 2:
            print("Jij kiest papier")
        elif pvc == 3:
            print("Jij kiest schaar")
        print("Het is gelijkspel")
    elif pvc == 1:
        print("{} kiest steen".format(name1))
        if pvp == 3:
            print ("Gefeliciteerd {} jij wint".format(name1))
        else:
            print("Helaas {}, je hebt verloren".format(name1))
    elif pvc == 2:
        print("{} kiest papier".format(name1))
        if pvp == 1:
            print ("Gefeliciteerd {} jij wint".format(name1))
        else:
            print("Helaas {}, je hebt verloren".format(name1))
    elif pvc == 3:
        print("{} kiest schaar".format(name1))
        if pvp == 2:
            print ("Gefeliciteerd {} jij wint".format(name1))
        else:
            print("Helaas {}, je hebt verloren".format(name1))
    else:
        print("De door jou genomen keuzen wordt niet herkend ")

# een welkom menu met opties zoals 1p, 2p, 3p of stoppen(exit)
print("Welkom Wat is je naam?")
name1 = input("mijn naam is: ")
toevoegen = namePlayArr[0] #de input wordt in de 2d array geplaats
toevoegen.append(name1) #de input wordt in de 2d array geplaats
print ("\nWelkom {} bij steen papier schaar! Maak een keuze door middel van een cijfer te antwoorden.".format(name1))

# een loop zodat het spel nooit zich zelf afsluit tenzij de gebruiker daar voor kiest
keuzeMenu = True
while keuzeMenu:
    keuze = int(input("\nmaak een keuze {}.\n1. Player vs pc\n2. Player vs player\n3. 3 Player game\n4. Exit\n\n".format(name1)))
    if keuze == 1:   
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
        print("Welkom player 2 Wat is je naam?")
        name2 = input("mijn naam is: ")
        toevoegen = namePlayArr[0] #de input wordt in de 2d array geplaats
        toevoegen.append(name2) #de input wordt in de 2d array geplaats       
        tweePlayerGame =  True
        while tweePlayerGame: # een loop zodat het spel aanblijft tot iemand heeft gewonnen
            pvc = int(input("\n{} maak een keuze\n1. steen\n2. papier\n3. schaar\n\n".format(name1)))
            clear()
            pvp = int(input("\n{} maak een keuze\n1. steen\n2. papier\n3. schaar\n\n".format(name2)))
            clear()
            weegschaal2P()
    elif keuze == 3:
        # een loop voor de 3p spel
        driePlayerGame = True
        print("3 player game is op dit moment onder contstructie.")
    elif keuze == 4:
        print("\ntot de volgende keer {}!".format(name1))
        keuzeMenu = False
    else:
        print("\nDe door jou genomen keuzen wordt niet herkend {}. Maak keuze uit 1, 2, 3 of 4\n".format(name1))
