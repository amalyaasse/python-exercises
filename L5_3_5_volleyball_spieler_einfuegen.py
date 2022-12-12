kader = ["Armin","Batu","Kai", "Sven", "Paul", "Milan","Goran", "Chris", "Nico", "Dennis", "Emin", "Luca"]

def kader_ausgeben():
    print("Kader")
    for i in range(len(kader)):
        print(kader[i])
        
def einfügen_spieler():
    index = int(input("in welche stelle möchten Sie neue Sieler hinzufügen:"))
    name = input("geben Sie der Name des neuen Spielers an:")
    
    kader[index -1] = name
    for i in range (len(kader)):
        print (kader[i])
    
einfügen_spieler()