#Alle Zahlen aus dem Zahlenbereich 1-1000, die durch 15 oder 25 teilbar sind, auf dem Bildschirm ausgeben

for x in range (1, 1001):
    if (x % 15 == 0) or (x % 25 == 0):
        print (x)