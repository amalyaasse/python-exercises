#Lesen Sie das Programm und sagen Sie vorher, welche Bildschirmausgabe das Programm erzeugen wird

def funktion(zahl_1, zahl_2):
    zahl_3 = zahl_1*zahl_2
    zahl_4 = zahl_3 % 4
    return zahl_4*2

for i in range(2, 17, 3):
    ergebnis                                                                                                                                                                                                                                                                                          = funktion(i, i+2)
    print(ergebnis)