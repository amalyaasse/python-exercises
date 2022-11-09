#Auf einem Sparbuch wird ein Geldbetrag angelegt. Für diesen Betrag gibt es
#einen bestimmten Zinssatz. In diesem Projekt soll überprüt werden, wie viele
#Jahre es dauert, bis dieser Betrag einen bestmmten Zielwert erreicht oder
#überschreitet. Dabei sollen die Jahresendwerte der Finanzanlage jeweils ausgegeben
#werden.
#(Zinseszinsen nicht vergessen)

Betrag = float(input("Welcher Betrag soll angelegt werden? "))
zinssatz = float(input("Zu welchem prozentualen Zinssatz wird verzinst? "))
zielwert = float(input("Welcher Zielwert soll erreicht werden? "))
jahr = 0
while Betrag < zielwert:
    Betrag = Betrag * (1 + (zinssatz / 100))
    jahr = jahr + 1
print("Nach", jahr, "jahren wird", Betrag, "Ziel erreicht")