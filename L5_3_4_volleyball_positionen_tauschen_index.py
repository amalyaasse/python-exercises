spieler = ["Armin","Batu","Kai","Sven","Paul", "Milan"]

def startaufstellung_ausgeben():
    print("Neue Startaufstellung")
    for i in range (len(spieler)):
        print(spieler[i])


def manschaft_umstellen_pos():
    a = int(input("welche Platz möchten Sie umstellen: "))
    b = int(input("welche Platz möchten Sie umstellen: "))
    spieler[a] = spieler[b]
    for i in range(len(spieler)):
        print(spieler[i])
    
    
    
    
# Funktionsauufruf
startaufstellung_ausgeben()
manschaft_umstellen_pos()