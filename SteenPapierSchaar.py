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

# 2d array [[playernaam, playernaam, playernaam],[punten p1, punten p2, punten p3]]
namePlayArr = [["a", "b", "c"],[0, 0, 0]]

# een welkom menu met opties zoals 1p, 2p, 3p of stoppen(exit)
print("Welkom Wat is je naam?")
name1 = input("mijn naam is: ")

print ("\nWelkom {} bij steen papier schaar! Maak een keuze door middel van een cijfer te antwoorden.\n ".format(name1))
namePlayArr[0] = name1 #de naam wordt geplaats in de array

# een loop zodat het spel nooit zich zelf afsluit tenzij de gebruiker daar voor kiest
keuzeMenu = True
while keuzeMenu:
    keuze = input(int("Maak een keuze {}.\n1. Player vs pc\n2. Player vs player\n3. 3 Player game\n4. Exit\n\n".format(name1)))
    if keuze == 1:
        print("a")
    if keuze == 2:
        print("2")
    if keuze == 3:
        print("3")
    if keuze == 4:
        print("tot de volgende keer {}!")
        keuzeMenu = False
    else:
        print("\nDe door jou genomen keuzen wordt niet herkernt {}. Maak keuze uit 1, 2, 3 of 4\n".format(name1))

# 1d array [rondex, rondex, rondex, rondex]
# een functie die weegt wie wint. Steen papier of schaar.
# een functie die random steen, papier of schaar genereerd als de gebruiker tegen de pc speelt
# een loop zodat het spel aanblijft tot iemand heeft gewonnen
# een loop voor de 1p spel
# een loop voor de 2p spel
# een loop voor de 3p spel

