#Der Trainer der Mannschaft möchte eine Software, mit deren Hilfe er sich die Namen
#der Stammspieler, die der Ersatzspielerund die des gesamten Kaders anzeigen lassen kann.
#Der Co-Trainier hat bereits mit der Implementierung der Eingabe begonnen(siehe Vorlage).
#Es steht nur noch die Implementierung der Funktionen aus
#Implementieren Sie
#•eine Funktion zeigeStartaufstellung(), mit der die Namen der Stammspieler
#•eine FunktionzeigeErsatzspieler(), mit der die Namen der Ersatzspieler
#•eine Funktion zeigeKader(), mit der die Namen aller Spieler im Kader der Mannschaftin der Konsole angezeigt werden 

spieler =["Armin", "Batu", "Kai", "Sven", "Paul", "Milan"]
ersatz = ["Chris", "Denis", "Emin", "Goran", "Luca", "Nico"]
Kader = spieler + ersatz
#print(Kader[10])
#print(len(Kader))
def zeigeStartaufstellung():
    platz = int(input("Welche Platzierung soll ausgegeben werden in Liste Spieler (1-8)?"))
    for  i in range(len(spieler[platz-1])):
        print(spieler[i])
    
 
def FunktionzeigeErsatzspieler():
    platz = int(input("Welche Platzierung soll ausgegeben werden in Liste Ersatz (1-8)?"))
    for i in range(len(ersatz)):
       print(ersatz[i])
   
def zeigeKader():
    platz = int(input("Welche Platzierung soll ausgegeben werden in Liste Kader (1-8)?"))
    for i in range(len(Kader)):
        print(Kader[i])
print("*****************************************************************")       
print("die Namen der Stammspieler")
print("*****************************************************************")
zeigeStartaufstellung()
print("*****************************************************************")
print("die Namen der Ersatzspieler")
print("*****************************************************************")
FunktionzeigeErsatzspieler()
print("*****************************************************************")
print("die Namen aller Spieler im Kader")
print("*****************************************************************")
zeigeKader()
        
    

