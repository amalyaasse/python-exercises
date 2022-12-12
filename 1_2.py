# Bakterienkultur wächst jede Stunde 8%
#zu bBeginn bedeckt Sie eine Fläche von 5.6 qcm
#Nach 24 Stunden bedeckt--- ?

Fläche = 5.6
for x in range(1, 25):
    Fläche = Fläche + Fläche*0.08
    print("Fläche nach", x,"h:", Fläche)
    