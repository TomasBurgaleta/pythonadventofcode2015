from Dial import Dial
dial =  Dial(50)
total = 0
totalClicks = 0
with open("data01.txt", "r") as archivo:
#with open("example.txt", "r") as archivo:
    print(dial)
    for lineaEnBruto in archivo:
        linea = lineaEnBruto.strip()
        letra = linea[:1]
        numero= linea[1:]
        if letra == "R":
            totalClicks = totalClicks + dial.rotationWithClick(True, int(numero))
        else:
            totalClicks = totalClicks + dial.rotationWithClick(False, int(numero))
        if dial.x == 0:
            total = total + 1
        print(linea)
        print(dial)
        print(total)
        print(totalClicks)
        print("----------")


print(total)
print(totalClicks)
print(total + totalClicks)
# 969
# 4918
# 5887