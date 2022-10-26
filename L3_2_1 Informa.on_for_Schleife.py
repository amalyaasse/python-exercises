#Schreiben Sie ein Programm, das den Betrag des Taschengelds in
#Abhängigkeit vom Alter ausgibt.
#Das Taschengeld wird vom 6. bis zum 21. Lebensjahr ausgezahlt.
#Dabei sind der Anfangsbetrag und die jährliche Erhöhung vom Benutzer einzugeben

Alter_Kind = float(input("geben Sie Alter ihres Kindes an: "))
Anfangsbetrag = 100
Jährliche_Erhöhung = 50
for Alter_Kind in range(6, 21):
    Taschengeld = Anfangsbetrag + Jährliche_Erhöhung
print(Taschengeld)


