#Es sollen drei Zahlen eingegeben werden
#daraus soll die kleinste Zahl ermittelt werden
x = input()
y = input()
z = input()

if (x<y)&(x<z):
    print("die kleinste zahl ist: ", x)
elif (y<x)&(y<z):
    print("die kleinste zahl ist: ", y)
else:
    print("die kleinste zahl ist: ", z)