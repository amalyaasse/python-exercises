#In diesem Projekt soll überprüB werden, ob ein Besucher
#eines Tierparks ein Kind (bis 12 Jahre) oder ein Senior (ab 60 Jahre) ist.
#Kinder und Senioren zahlen 8,00 Euro EintriP,
#für alle anderen beträgt der EintriPspreis 12,00 Euro

Age_Person = float(input("Geben Sie Ihre Alte an: "))

if Age_Person <=12 or Age_Person >=60:
    print("Eintritt kostet 8 Euro für Sie")
    
else:
    print("Eintritt kostet 12 Euro für Sie")