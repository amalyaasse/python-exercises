#Der Eintritt ins Schwimmbad kostet 5.40 Euro für Erwachsene und
#3.20 Euro für Personen unter 16 Jahren.
#1. Erstellen Sie ein Programm, das nach dem Alter fragt
#und den korrekten Eintrittspreis ausgibt

Age = int(input("geben Sie Ihre Alter an: "))

if Age > 16:
    print("Der Eintritt ins Schwimmbad kostet 5.40 Euro")
else:
    print("Der Eintritt ins Schwimmbad kostet 3.20 Euro")