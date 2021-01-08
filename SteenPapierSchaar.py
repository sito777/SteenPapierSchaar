""" De opdracht
Je gaat steen papier schaar namaken. De regels hiervan zijn bekent maar voor de applicatie moet er 
een winnaar komen uit een best of 3! (de eerste met 2 punten uit 3 wint). Evenals moet de data worden 
opgeslagen van degene die heeft gewonnen, met welk voorwerp en hoeveel punten op dat moment.

Eisen V:
De applicatie blijft aanstaan tot er iemand heeft gewonnen met 2 punten
De applicatie is werkend en het spel kan gespeeld worden
De applicatie heeft 2 functies
De applicatie bevat een 1D & 2D array
De applicatie kan met 2 spelers gespeeld worden met invoer eigen naam
De applicatie wordt optijd opgeleverd
Nette code (variabele)

Eisen G:
Al het bovenstaande
Er kan met 3 spelers tegelijk gespeeld worden
Goede code comments
"""
from array import *
import random

import os
def clear(): os.system('clear') #on Linux System
clear()

# 1d array [rondex, rondex, rondex, rondex]
ronde = [1, 2, 3, 4]


# 2d array [[playernaam, playernaam, playernaam],[punten p1, punten p2, punten p3]]
namePlayArr = [["a", "b", "c"],[0, 0, 0]]

# de waarde vaan sps
steen = 1
papier = 2
schaar = 3

def playerwin():
    print("je hebt gewonnen van de pc")

def pcwin():
    print("Helaas de pc heeft gewonnen van jou")

def gelijkspel():
    print("gelijk spel)

# een functie die random steen, papier of schaar genereerd als de gebruiker tegen de pc speelt
def pckeuze():
    sps = [1,2,3]
    com = random.choice(sps)
    if com == 1:
        print("steen")
    if com == 2:
        print("papier")
    if com == 3:
        print("schaar")    
    return com 

# een functie die weegt wie wint. Steen papier of schaar.
def weegschaal():
    # als player 1 wint
    if pvc == 1 and com == 3:
        playerwin()
    elif pvc == 2 and com == 1:
        playerwin()
    elif pvc == 3 and com == 2:
        playerwin()
    # als de pc wint
    elif pvc == 3 and com == 1:
        pcwin()
    elif pvc == 2 and com == 3:
        pcwin()
    elif pvc == 1 and com == 2:
        pcwin()
    # gelijkspel
    elif pvc == 1 and com == 1:
        gelijkspel()
    elif pvc == 2 and com == 2:
        gelijkspel()
    elif pvc == 3 and com == 3:
        gelijkspel() 
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
    keuze = int(input("\nMaak een keuze {}.\n1. Player vs pc\n2. Player vs player\n3. 3 Player game\n4. Exit\n\r".format(name1)))
    if keuze == 1:   
        # een loop voor de 1p spel
        eenPlayerGame =  True
        while eenPlayerGame: # een loop zodat het spel aanblijft tot iemand heeft gewonnen
            pvc = int(input("\n{} Maak een keuze\n1. steen\n2. papier\n3. schaar\n".format(name1)))
            sps = [1,2,3]
            com = random.choice(sps)
            weegschaal()
    elif keuze == 2:
        # een loop voor de 2p spel
        tweePlayerGame =  True
        while tweePlayerGame: # een loop zodat het spel aanblijft tot iemand heeft gewonnen
            x = y   

    elif keuze == 3:
        # een loop voor de 3p spel
        driePlayerGame = True
        while driePlayerGame: # een loop zodat het spel aanblijft tot iemand heeft gewonnen
            x = y

    elif keuze == 4:
        print("\ntot de volgende keer {}!".format(name1))
        keuzeMenu = False

    else:
        print("\nDe door jou genomen keuzen wordt niet herkend {}. Maak keuze uit 1, 2, 3 of 4\n".format(name1))
