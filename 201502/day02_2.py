floor = 0
numlineas = 0
totalBow = 0
totalWrap = 0
with open("data02.txt", "r") as archivo:
    for linea in archivo:
        numlineas += 1
        dimensionBox = linea.split("x")

        dimensionBox = [int(x) for x in dimensionBox] # conversion a ints

        maxValue = max(dimensionBox[0], dimensionBox[1], dimensionBox[2])
        totalRibbon = 0
        numPerimeter = 0
        wrap = dimensionBox[0] * dimensionBox[1] * dimensionBox[2]
        for distance in dimensionBox :
            if distance < maxValue :
                totalRibbon = totalRibbon + (2 * distance)
                numPerimeter += 1

        if numPerimeter == 0:
            totalRibbon = 4 * maxValue
        if numPerimeter == 1:
            totalRibbon = totalRibbon + (2 * maxValue)
        totalBow = totalBow + totalRibbon
        totalWrap = totalWrap + wrap
        print("num linea -> " + str(numlineas) +  " con valor " + linea.strip() +" se suma " + str(totalRibbon) + " total : " + str(totalBow))

print(totalBow + totalWrap)