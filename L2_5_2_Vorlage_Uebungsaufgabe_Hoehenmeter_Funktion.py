#Die Siedetemperatur von Wasser beträgt auf Höhe des Meeresspiegels 100o Celsius.
#Bei zunehmender Höhe verringert sich die Siedetemperatur um 1o Celsius pro 300 Höhenmeter.
#Entwerfen Sie ein Programm, mit dem man mithilfe der Siedetemperatur des Wassers die aktuelle
#Höhe besHmmen kann. Auf welcher Höhe befinden
#Sie sich, wenn das Wasser bei 89o Celsius zu kochen
#beginnt?Die Eingabe der Daten soll am Bildschirm erfolgen. */
#ändern Sie es so ab, dass für die Berechnung der Höhe eine FunkQon berechne_hoehe()benutzt wird.
#Diese empfängt als Parameter die Siedetem-peratur, berechnet daraus die Höhe und gibt diese Höhe
#als Rückgabewert zurück. Im Hauptprogramm soll der Benutzer zur Eingabe der Siedetemperatur
#aufgefordert werden, danach die FunkQon berechne_hoehe()aufgerufen werden und ihr Rückgabewert
#in einer Variablen hoeheabgespeichert werden. Abschließend soll die errechnete
#Höhe mit einem kleinen Erläuterungstext ausgegeben werden.

Siedetemp = float(input("Bitte gebe Sie Siedetemperatur in Celsius An C = "))

if Siedetemp == 100:
    print("Höhe = 0 also du befindest dich auf Höhe des Meeresspiegels") 
elif Siedetemp < 100:
    a = 100 - Siedetemp
    b = 300*a
    print("Du befindest dich auf Höhe = ",b)
