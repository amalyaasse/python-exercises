alter = int(input("bitte alter eingeben: "))
TheorieStunden = int(input("Bitte Anzahl der Theoriestunde eingeben: "))

if alter >=17 and TheorieStunden >=16:
    print("Sie sind zur Prüfung zugelassen")
else:
    print("nicht zugelassen")