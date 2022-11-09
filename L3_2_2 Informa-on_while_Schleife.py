#Der Fischbestand eines Teichs beträgt zu Beginn eines Jahres drei Fische.
#Jedes Jahr verdoppelt sich der Fischbestand. Erstellen Sie ein Programm,
#das die Dauer in Jahren ermitelt, bis ein bestmmter, vom Anwender
#ein-zugebender Fischbestand erreicht bzw.
#überschriten wird
jahre = 1
Fischbestand = 3
Erwünschte_Fischbestand = float(input("geben Sie erwünschte Fischbestand an: "))
while Fischbestand <= Erwünschte_Fischbestand:
     Fischbestand = 2*Fischbestand 
     jahre +=1
print("Erst nach", jahre, "jahren gibt es ", Erwünschte_Fischbestand, "Fische" )
#print("es gibt jetzt genug Fische zum fangen :)")
