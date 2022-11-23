#Entwickle ein Programm, welches das Einmaleins
#für eine eingegebene Zahl ausgibt!

Zahl = int(input("geben Sie der Zahl an: "))
for x in range(1,11):
    Produkt= Zahl*x
    print (x,"*",Zahl,"=", Produkt)
