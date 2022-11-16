#Das Taschengeld von Fritzchen soll neu festgelegt werden. Er macht seinem Vater folgenden
#Vorschlag: Papa, du gibst mir die erste Woche nur einen Cent. In jeder weiteren Woche erhalte
#ich den doppelten Betrag der vergangenen Woche.“ Nach wieviel Monaten übersteigt Fritzchens
#Taschengeld das Einkommen seines Vaters (Nettogehalt: 2500 Euro)? (Annahme: 1 Monat  = 4 Wochen)

Taschengeld = 0.01
woche = 1

while Taschengeld < 2500:
    Taschengeld = Taschengeld*2
    woche = woche + 1
else:
    monate = woche/4
    print ("nach", woche, "woche wird Fritzchens Taschengeld das Einkomen seines Vaters übersteigt")
    print ("das sind", monate)

