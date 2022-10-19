#Schreiben Sie ein Programm, das den Umfang und den Flächeninhalt eines Rechtecks berechnet.
#Der Benutzer gibt dazu die Länge und die Breite des Rechtecks ein.
#Das Programm berechnet die Ergebnis-se und gibt diese aus

a = float(input("Bitte geben Sie die Länge von Rechtecks an a = "))
b = float(input("Bitte geben Sie die Breite des Rechtecks an b = "))
Fläche = a*b
Umfang = 2*(a+b)
print("Fläche = ",Fläche)
print("Umfang = ",Umfang)