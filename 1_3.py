# alle gerade zahlen zwischen 1 und 1000, die zugleich auch durch 14 teilbar sind, auf dem Bildschirm ausgeben

for x in range(1, 1001):
    if (x % 2 == 0) and (x % 14 == 0):
        print(x)