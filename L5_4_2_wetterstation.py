Wochentage = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Sammstag","Sonntag"]
Temperatur= []


for i in range(len(Wochentage)):
    print(Wochentage[i])
    Temp=int(input("Die Temperatur:"))
    Temperatur.append(Temp)

#Deklaration und initialiezierung den Variabeln
maxT = Temperatur[0]
minT = Temperatur[0]
Temp = Temperatur[0] #Durchschnittliche Temperatur

#Höhste Temperatur
if Temperatur[i] > maxT:
       maxT = Temperatur[i]

#niedrigste Temperatur
if Temperatur[i] < minT:
    minT = Temperatur[i]
    

print("Höhste Temperatur: ", maxT)
print("Niedrigste Temperatur: ",minT)
print("Temperaturunterschied: ", maxT-minT)

    