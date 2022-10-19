#n diesem Projekt können Gebote für einen zum Kauf angebotenen Artikel abgegeben werden.
#In dem Programmcode ist der Mindestpreis (hier 24.99) hinterlegt. Ist der von dem Anwender
#vorgeschlagene Kaufpreis geringer, wird der Text „Ihr Angebotspreis liegt unterhalb des Mindestpreises!“
#ausgegeben. Andernfalls erscheint der Text
#„Herzlichen Glückwunsch, Sie haben den Ar;kel erworben!“.

Mindesprise = 24.99
Kaufpr = float(input("Bitte geben Sie Ihre Vorgeschlagene Kaufprise ="))#Vorgeshlagene Kaufpreise
if Kaufpr < 24.99:
    print("Ihr Angebotspreis liegt unterhalb des Mindestpreises")
else:
    print("Herzlichen Glückwunsch, Sie haben den Artikel erworben!")

