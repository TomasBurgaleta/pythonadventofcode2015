floor = 0
numlineas = 0
numSteps = 0
with open("data01.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
        print(numlineas)
        for caracter in linea:
            numSteps += 1
            if caracter == "(":
                floor += 1
            else:
                if caracter == ")":
                    floor -= 1
                else:
                    print(caracter)
            if floor == -1:
                print(numSteps)

    print(floor)