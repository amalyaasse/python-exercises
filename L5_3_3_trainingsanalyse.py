#Im Training für die Vereinsmeisterschaften wirft jeder Dartspieler 6 Pfeile auf die Dartscheibe bevor
#der nächste Dartspieler an der Reihe ist. Sie sollen ein Programm schreiben, dasaufgrund der 6geworfenen
#Pfeile eine Analyse durchführt. Es sollen folgende Angaben in der Konsoleausgegeben werden: Höchste Punktzahl,
#niedrigste Punktzahl und die durchschnittliche Punktzahl.Die Eingaben der Wurfergebnisse erfolgtenebenfalls
#über die Konsole(Beieinem Wurf sind maximal 60 Punkte erreichbar.
import random


wurf = [] #Deklaration und initialiesierung leeres Array 


for i in range (6):  #The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
    Punktzahl = random.randint(1,60)
    wurf.append(Punktzahl)
    print("Wurf ",i+1,":", wurf[i])
    
#Deklaration und Initialiesierung den Variabeln
maxP = wurf[0]
minP = wurf[0]
summeP = 0

#Bester Wurf
for i in range(6):
     if wurf[i] > maxP:
         maxP = wurf[i]
         
#Schlechteste Wurf
for i in range(6):
    if wurf[i] < minP:
        minP = wurf[i]
        
#Durchnitliche Wurf
for i in range(6):
    summeP = summeP + wurf[i]
     
mittelP = summeP / 6
        
   #Ausgabe      
print("Bester Wurf", maxP)
print("Schlechtster Wurf: ", minP)
print ("Durchschnittliche Punktzahl: ", mittelP)
    

