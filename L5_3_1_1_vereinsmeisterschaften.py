#Der Mühlberger SC möchte die Ergebnisse des Wett-kampfs veröffentlichen. Nutzer sollen die Möglichkeit haben,
#sich an einem Computer eine Platzie-rung ausgeben zu lassen. Möchte der Nutzer den Erstplatzierten ausgegeben bekommen,
#muss er bspw. eine „1“ eingeben. Außerdem soll die Teilnehmerzahl angezeigt werden.
#Die Teilnehmer an der Meisterschaft sind in dem Array platzierungenin der Reihenfolge ihrer Platzierung gespeichert.


platzierungen = ["Matthias Schmitt", "Felix Holzmann", "Sabrina Eggers", "Sebastian Wolf", "Niklas Eisenbaum",
                 "Florian Kuster", "Jan Ackerman", "Erika Ebersbacher"]

platz = int(input("Welche Platzierung soll ausgegeben werden (1-8)?"))
print("Platzierung", platz, ":", platzierungen[platz-1])
print("Teilnehmeranzahl:", len(platzierungen))