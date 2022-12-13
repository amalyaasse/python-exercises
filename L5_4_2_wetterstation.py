Wochentage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Sammstag","Sonntag"]
Temperatur= []


for i in range(len(Wochentage)):
    print(Wochentage[i])
    Temp=float(input("Die Temperatur:"))
    Temperatur.append(Temp)

#Deklaration und initialiezierung den Variabeln
maxT = Temperatur[0]
minT = Temperatur[0]
summe = 0 #Durchschnittliche Temperatur

#Höhste Temperatur
for i in range(len(Temperatur)):
    if Temperatur[i] > maxT:
       maxT = Temperatur[i]

#niedrigste Temperatur
for i in range(len(Temperatur)):
    if Temperatur[i] < minT:
        minT = Temperatur[i]
    
#durchschnittliche Temperatur
    
for i in range(len(Temperatur)):
    summe = summe + Temperatur[i]

MittelTemp = summe/len(Temperatur)



print("Höhste Temperatur: ", maxT)
print("Niedrigste Temperatur: ",minT)
print("Temperaturunterschied: ", maxT-minT)
print("Durchschnittliche Temperatur: ", MittelTemp)

    