#ändern Sie der Aufgabe L2_4_3 so ab, dass für die Berechnung der Höhe eine Funktion berechne_hoehe()benutzt wird.
#Diese empfängt als Parameter die Siedetemperatur, berechnet daraus die Höhe und gibt diese Höhe als Rückgabewert zurück.
#Im Hauptprogramm soll der Benutzer zur Eingabe der Siedetemperatur aufgefordert werden,
#danach die FunkQon berechne_hoehe()aufgerufen werden und ihr Rückgabewert in einer Variablen hoeheabgespeichert werden.
#Abschließend soll die errechnete Höhe mit einem kleinen Erläuterungstext ausgegeben werden.

Siedtemp = float(input("Bitte gebe Sie Siedetemperatur in Celsius An C = "))

def berechne_hoehe(Siedtemp):
    if Siedtemp == 100:
        Hoehe = 0
    elif Siedtemp < 100:
        a = 100 - Siedtemp #Unterschied von Normalsiedtemperatur bestimmen
        Hoehe = 300*a #Unterschied mit 300 multiplizieren, um Höhe zu bestimmen
    else:
        Hoehe = "die niedriege ist "
    return Hoehe
Ergebniss = berechne_hoehe(Siedtemp)
print("Du befindest dich auf Hoehe ",Ergebniss, "von Meeresspiegels")

