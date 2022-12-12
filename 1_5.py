# alle Zahlen aus dem Zahlenbereich 0 bis 1000, die durch 6 und gleichzeitig 10 teilbar sind
# oder durch 12 und gleichzeitig 18 teilbar sind

for x in range(0, 1001):
    if (x % 6 == 0) and (x % 10 == 0):
        print(x)
    elif (x % 12 == 0) and (x % 18 == 0):
        print(x)
    
