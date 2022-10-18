from tkinter import *

def berechnen():
    zahl_1 = float(tf_zahl1.get())
    ergebnis = zahl_1*2
    lb_ergebnis_ausgabe.config(text = ergebnis)

fenster = Tk()
fenster.title("Beispiel-GUI")

lb_zahl1 = Label(fenster, text = "Zahl eingeben: ")
lb_zahl1.grid(row = 0, column = 0)
tf_zahl1 = Entry(fenster)
tf_zahl1.grid(row = 0, column = 1)
lb_ergebnis = Label(fenster, text = "Verdoppelung: ")
lb_ergebnis.grid(row = 1, column = 0)
lb_ergebnis_ausgabe = Label(fenster,bg = "white", width = 17, anchor = W, relief = SUNKEN)
lb_ergebnis_ausgabe.grid(row = 1, column = 1)
bt_umrechnen = Button(fenster, text = "Berechnung starten", command = berechnen)
bt_umrechnen.grid(row = 2, column = 1)