#In diesem Projekt soll überprüB werden, ob eine Anmeldung zur
#Führerscheinprüfung möglich ist oder nicht.
#Die Bedingung für eine Zulassung lautet wie folgt: Der Fahrschüler muss
#mindestens 17 Jahre alt sein und mindestens 16 Theoriestunden absolviert haben

Age_Person = float(input("geben Sie Ihre alter an: "))
Th = float(input("geben Sie Anzahl Ihre Theoriestunden an: "))

if (Age_Person >=17) and (Th >= 16):
    print("Führerscheinprüfung ist möglich")
else:
    print ("Führerscheinprüfung ist nicht möglisch")