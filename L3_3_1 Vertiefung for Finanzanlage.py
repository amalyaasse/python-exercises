#Vertifungsaufgabe: for-Schleife  –  Finanzanlage
#In diesem Projekt soll überprüft werden, welchen Zielwert eine Finanzanlage,
#die zu einem bestimmten Zinssatz für eine bestimme Anlagedauer (in Jahren)
#durch Zinseszins-Vermehrung erreicht. Für jedes Jahr, die die Finanzanlage läuft,
#soll der Wert am Ende des Jahres ausgegeben werden

Kapital = float(input("Geben Sie den Betrag an: "))
Zinssatz = int(input("Geben Sie Zinsatz an: "))
Anlagedauer = int(input("Geben Sie Anlagedauer in Jahren an: "))
for Anlagedauer in range (1, Anlagedauer+1):
    Kapital = Kapital*(1 + Zinssatz/100)
    print("In", Anlagedauer,  "jahren hat Kapital durch Zinseszins-Vermehrung:", Kapital, "erreicht")

