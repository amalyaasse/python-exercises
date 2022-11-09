#Schreiben Sie ein Programm, das den Betrag des Taschengelds in
#Abhängigkeit vom Alter ausgibt.
#Das Taschengeld wird vom 6. bis zum 21. Lebensjahr ausgezahlt.
#Dabei sind der Anfangsbetrag und die jährliche Erhöhung vom Benutzer einzugeben

Alter_Kind = int(input("geben Sie Alter ihres Kindes an: "))
Taschengeld = float(input("Taschengeld eingeben:  "))
Jährliche_Erhöhung = float(input("Jährliche Erhöhung: "))

for i in range(Alter_Kind+1, 21): #Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
    Taschengeld = Taschengeld + Jährliche_Erhöhung
    print("wenn Ihre Kind", i,". jahre alt ist, dann bekommt :",Taschengeld,"EUR")
else:
    print("Das kind muss zwischen 6 und 21 Jahre sein, sonnst gibt es kein ")

