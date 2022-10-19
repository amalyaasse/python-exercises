#Schreiben Sie ein Programm, das den Mietzuschuss in Abhängigkeit vom Mietpreis berechnet.
#Bei einer Miete von weniger als 500,00 Euro beträgt der Zuschuss 2%. Von 500,00 Euro bis unter
#1000,00 Euro beträgt der Zuschuss 5% und ab 1000,00 Euro erhält man einen Zuschuss von 7%

M = float(input("Geben Sie bitte Ihre Mietpreis an = "))#Mietpreise

if M < 500:
    Zuschuss = M*(2/100)
    print(Zuschuss)

elif (M >= 500)&(M < 1000):
    Zuschuss = M*(5/100)
    print(Zuschuss)
elif M >= 1000:
    Zuschuss = M*(7/100)
    print(Zuschuss)
    
    