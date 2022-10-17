#Zufalzahlen zwischen 1 und 6 generieren bis einen 6 kommt
#Das Programm gibt dann die gewürfelte zahlen und
#die Anzahl der Würfe zurück

#Zahlgenerator

import random
Wurfel_zahl = random.randint(1,6)
Anzahl_Versuch = 0 # initialisation and declaration für anzahl der Versuche
Versuche = [] #array ist initialiesiert und declariert 

while Wurfel_zahl != 6:
    Wurfel_zahl = random.randint(1,6)
    Versuche.append(Wurfel_zahl)
    Anzahl_Versuch = Anzahl_Versuch + 1
print(Versuche)
print("Anzahl der Versuche sind: ", Anzahl_Versuch)
print("Unsere erwünschte Wurfelzahl: ", Wurfel_zahl ,"ist also beim", Anzahl_Versuch, ".te Versuch getroffen")
print("Wollen sie es noch einmal spielen :) viel spaß")
