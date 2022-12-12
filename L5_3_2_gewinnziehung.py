#Am Abend des Dart-Events findet die Ziehung der Gewinnerlose statt. Der Ziehungsleiter soll die Möglichkeit
#erhalten, die gezogenen Losnummern in einem Array zu speichern.
#Nachdem die fünf Losnummern mit Gewinnen gezogen worden sind, sollen sie ausgegeben werden.

import random

#Initialisierung und Deklaration leeres Array
losnummern = []

#Einlesen von 5 Gewinnerlosen
print("----Gewinnlose-----")

for i in range (0,4):
    gezogene_num = random.randint(1000, 9999)
    losnummern.append(gezogene_num)
    print ("Gezogene Losnummer: ",losnummern[i])
    







