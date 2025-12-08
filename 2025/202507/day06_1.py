



#with open("example.txt", "r") as archivo:
with open("data01.txt", "r") as archivo:
    filas = [x for x in archivo.readlines()]
    beams = []
    spliters = []
    indice_inicio = filas[0].find("S")
    fila_inicio = filas[1]
    filas[1] = fila_inicio[:indice_inicio] + "|" + fila_inicio[indice_inicio + 1:]
    suma = 0
    for indice_fila in range (1, len(filas)):
        fila = filas[indice_fila]
        fila_anterior = filas[indice_fila -1]
        spliters = [i for i, v in enumerate(fila) if v == '^']
        beams = [i for i, v in enumerate(fila_anterior) if v == '|']
        for beam in beams:
            if fila[beam] == '^':
                fila = fila[:beam-1] + "|^|" + fila[beam + 2:]
                filas[indice_fila] = fila
                suma += 1
            elif fila[beam] == '.':
                fila = fila[:beam] + "|" + fila[beam + 1:]
                filas[indice_fila] = fila
        print(filas[indice_fila])
    print(suma)
