from Dial import Dial
dial =  Dial(50)
total = 0
with open("data01.txt", "r") as archivo:
#with open("example.txt", "r") as archivo:
    for linea in archivo:
        letra = linea[:1]
        numero= linea[1:]
        if letra == "R":
            dial.rotation(True, int(numero))
        else:
            dial.rotation(False, int(numero))
        print(linea + " : ")
        print(dial)
        if dial.x == 0:
            total = total + 1

print(dial)
print(total)