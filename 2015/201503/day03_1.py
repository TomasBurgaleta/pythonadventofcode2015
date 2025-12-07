import Point

floor = 0
numlineas = 0
grid = Point(0, 0)
with open("data01.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
        print(numlineas)
        for direction in linea:
            if caracter == "(":
                floor += 1
            else:
                if caracter == ")":
                    floor -= 1
                else:
                    print(caracter)

    print(floor)