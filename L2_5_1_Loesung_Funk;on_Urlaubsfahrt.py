#Benzinkosten für Ihre Urlaubsfahrt berechnet
#diese Berechnung soll in eine eigene Funktion ausgelagert werden
#benutzen Sie für dieses Programm eine Funktion mit Parameter und Rückgabewert.
#Folgende Parameter soll diese Funktion erhalten: Benzinpreis, Verbrauch des Autos, Länge der Strecke

def BenzKost(Benzinpreis, VerbrauchDesAutos, Strecke):
    BenzinkostenFürUrlaub = Benzinpreis*VerbrauchDesAutos*(Strecke/100)
    return BenzinkostenFürUrlaub

Benzinpreis = float(input("Benzinpreis = "))
VerbrauchDesAutos = float(input("Verbrauch des Autos pro 100km = "))
Strecke = float(input("Länge ders Strecke = "))
Ergebniss = BenzKost(Benzinpreis, VerbrauchDesAutos, Strecke)
print("Benzinkosten für Urlaub", Ergebniss)
    