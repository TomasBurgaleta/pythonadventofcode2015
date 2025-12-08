from Camino import Camino
import copy
import time

#9897897326778
mi_cache = {}
def busqueda_recursiva(filas, num_fila, columna):
    key = str(num_fila) + "," + str(columna)
    suma_caminos = 0
    if(num_fila <= 140) :
        suma_cache = mi_cache.get(key)
        if suma_cache is None:
            if (filas[num_fila])[columna] == '^' and (filas[num_fila -1 ])[columna] == '|':
                suma1 = busqueda_recursiva(filas, num_fila + 1, columna - 1)
                suma2 = busqueda_recursiva(filas, num_fila + 1, columna + 1)
                suma_cache = int(suma1) + int(suma2)
                mi_cache[key] = int(suma_cache)
                suma_caminos += suma_cache
                #print("creando cache ", key, " con valor ", suma_cache)
                if num_fila < 40:
                    print("nodo: ", num_fila, ",", columna, " suma : ", suma_caminos, " , suma1 + suma2 :", suma1, suma2)
            elif (filas[num_fila])[columna] == '|':
                suma = busqueda_recursiva(filas, num_fila + 1, columna)
                mi_cache[key] = suma
                suma_caminos += suma
                if num_fila < 40:
                    print("nodo: ", num_fila, ",", columna, " suma : ", suma_caminos)

        else:
            suma_caminos += suma_cache
    else:
        return 1
    return suma_caminos


#with open("example.txt", "r") as archivo:
with (open("data01.txt", "r") as archivo):
    filas = [x for x in archivo.readlines()]
    beams = []
    spliters = []
    indice_inicio = filas[0].find("S")
    fila_inicio = filas[1]
    filas[1] = fila_inicio[:indice_inicio] + "|" + fila_inicio[indice_inicio + 1:]
    for indice_fila in range (1, len(filas)):
        fila = filas[indice_fila]
        fila_anterior = filas[indice_fila -1]
        spliters = [i for i, v in enumerate(fila) if v == '^']
        beams = [i for i, v in enumerate(fila_anterior) if v == '|']
        for beam in beams:
            if fila[beam] == '^':
                fila = fila[:beam-1] + "|^|" + fila[beam + 2:]
                filas[indice_fila] = fila
            elif fila[beam] == '.':
                fila = fila[:beam] + "|" + fila[beam + 1:]
                filas[indice_fila] = fila
        print(filas[indice_fila])

    # fin de creacion de caminos en el dibujo

    columna_inicial = (filas[2]).find("^")
    suma = busqueda_recursiva(filas,2, columna_inicial)
    print("suma total " ,suma)