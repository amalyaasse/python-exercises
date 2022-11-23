#Erstelle ein Programm, das dem Nutzer in Abhängigkeit von Gewicht, Länge,
#Breite und Höhe eines Paketes
#den dazugehörigen Preis ausgibt. Dabei gibt es 3 Paketgrößen: Paket XS, Paket S, Paket M

Gewicht = float(input("geben Sie das Gewicht an: "))
Länge = float(input("Geben Sie die Länge an: "))
Breite = float(input("Geben Sie die Breite an: "))
Höhe = float(input("Geben Sie die Höhe an: "))

#Paket XS: Gewicht: maximal 1 kg Länge: maximal 30 cm Breite: maximal 30 cm Höhe: maximal 15 cm Porto: € 3.95

if Gewicht <= 1 and Länge <= 30 and Breite <= 30 and Höhe <= 15:
    Porto = 3.95
    print("paket xs, Porto beträgt : ",Porto, "Euro")

#Paket S:  Gewicht: maximal 2 kg Länge: maximal 60 cm Breite: maximal 30 cm Höhe: maximal 15 cm Porto: € 5.95
elif Gewicht <= 2 and Länge <= 60 and Breite <= 30 and Höhe <= 15:
    Porto = 5.95
    print("paket S, Porto beträgt : ",Porto, "Euro")
#Paket M:  Gewicht: maximal 5 kg Länge: maximal 120 cm Breite: maximal 60 cm Höhe: maximal 45 cm Porto: € 9.95
elif Gewicht <= 5 and Länge <= 120 and Breite <= 60 and Höhe <= 45:
    Porto = 9.95
    print("paket M, Porto beträgt : ",Porto, "Euro")
elif Gewicht >= 5 or Länge >= 120 or Breite >= 60 or Höhe >= 45:
    print("zu grosse Paket")



