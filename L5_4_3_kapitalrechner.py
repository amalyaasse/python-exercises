zinsen = [0.1, 0.2, 0.3, 0.3, 0.3, 0.4, 0.4, 0.5, 1]
jahre = int(input("Lafzeit mit Jahren: "))
Betrag = float(input("Geben Sie Ihre Betrag an: "))

if Betrag > 50000:
    for i in range(jahre):
        Betrag = Betrag + Betrag*zinsen[i] / 100
    print("Auszahlungsbetrag: ", Betrag, "Euro")
else:
    print("Der Betrag muss über 50.000 Euro sein")
