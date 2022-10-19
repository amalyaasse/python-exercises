#welcher Betrag zu zahlen ist, wenn eine Karte für den Abiball 30,00 Euro kostet
#und für Bestellungen von drei oder mehr Karten ein Rabatt von 20% gewährt wird.

Preise_der_Karte = 30;
Anzahl_der_Bestellung = float(input ("Bitte geben Sie Anzahl den bestellte Karten K= "))
if Anzahl_der_Bestellung >=3:
    Rabatt = (Anzahl_der_Bestellung*30)*(20/100)
    Preise_der_Karte = (Anzahl_der_Bestellung*30) - Rabatt
    print("Bezahlen Sie bitte",Preise_der_Karte, "Euro")
