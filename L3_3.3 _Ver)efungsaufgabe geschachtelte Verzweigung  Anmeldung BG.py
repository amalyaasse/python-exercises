#In diesem Projekt soll überprüft werden, ob eine Anmeldung mit einem mitlleren Bildungsabschluss an einem beruflichen
#Gymnasium in Baden-Würtemberg möglich ist oder nicht. Die Bedingungen dafür lauten wie folgt: Abschlusszeugnis
#(Mitlerer Bildungsabschluss) der Realschule, der zweijährigen Berufsfachschule, der BerufsauNauschule oder der
#Werkrealschule mit einem Notendurchschnit von mindestens 3,0 aus Deutsch, MathemaSk und Englisch
#(kein Fach schlechter als Note ausreichend)

Deutsch = int(input("Note in Fach Deutsch: "))
Englisch = int(input("Note in Fach Englisch: "))
Mathematik = int(input("Note in Fach Mathematik: "))

if Deutsch < 4 and Englisch <  4 and Mathematik < 4:
     print ("Die Aufnahme ist möglisch")
else:
    print("Aufnahme ist nicht möglisch")

