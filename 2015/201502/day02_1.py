floor = 0
numlineas = 0
total = 0
with open("data02.txt", "r") as archivo:
    for linea in archivo:
        numlineas += 1
        dimensionBox = linea.split("x")

        dimensionBox = [int(x) for x in dimensionBox] # conversion a ints
        area1 = (2*dimensionBox[0]*dimensionBox[1])
        area2 = (2*dimensionBox[1]*dimensionBox[2])
        area3 = (2*dimensionBox[2]*dimensionBox[0])
        minValue = min(area1, area2, area3)
        squarFeet = area1 + area2 + area3 + minValue/2
        total = total + squarFeet
        print("num linea -> " + str(numlineas) +  " con valor " + linea.strip() +" se suma " + str(squarFeet) + " total : " + str(total))

print(total)