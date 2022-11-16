#Der Eintritt ins Schwimmbad kostet 5.40 Euro für Erwachsene und
#3.20 Euro für Personen unter 16 Jahren.
#1. Erstellen Sie ein Programm, das nach dem Alter fragt
#und den korrekten Eintrittspreis ausgibt
#////////////////////////////////////////////////////
#2. (Zusatzfunktion, schwerer) Erweitern Sie das Programm so,
#dass es solange durchläuft, bis ein Wert von 0 eingegeben wird.
#Am Ende des Programms soll der Gesamtpreis für alle eingegebenen
#Personen ausgegeben werden. Mögliche Bildschirmausgabe:

Age = int(input("geben Sie Ihre Alter an: "))
gesamtKosten = 0

while Age != 0:
    if Age > 16:
        print("Der Eintritt ins Schwimmbad für Sie  kostet 5.40 Euro")
        gesamtKosten = gesamtKosten + 5.40
        Age = int(input("geben Sie Alter den andere Person an: "))
    else:
        print("Der Eintritt ins Schwimmbad für Sie kostet 3.20 Euro")
        Age = int(input("geben Sie Alter den andere Person an: "))
        gesamtKosten = gesamtKosten +3.20
print("Insgesamt mussen Sie ", gesamtKosten, "bezahlen")

    
   


