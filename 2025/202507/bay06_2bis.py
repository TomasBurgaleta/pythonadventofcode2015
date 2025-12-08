from Camino import Camino
import copy
import time

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

    set_caminos_finales = set()
    rutaInicial = Camino([])
    rutaInicial.nuevo_paso(int(filas[1].find('|'))) # añadimos ruta inicial
    set_caminos_finales.add(rutaInicial)
    print("total filas",len(filas))
    for indice_fila in range(2, len(filas)):
        inicio = time.time()
        fila = filas[indice_fila]
        fila_anterior = filas[indice_fila - 1]
        caminos_a_recorrer = list(set_caminos_finales)
        set_caminos_finales.clear()
        nuevos_caminos = list()
        for camino in caminos_a_recorrer:
            indice_paso = camino.ruta[indice_fila - 2]
            if fila[indice_paso] == '^':
                nuevo_camino = Camino(camino.ruta[:])
                nuevo_camino.nuevo_paso(indice_paso -1)
                nuevos_caminos.append(nuevo_camino)
                camino.nuevo_paso(indice_paso + 1)
                nuevos_caminos.append(camino)
            elif fila[indice_paso] == '|' :
                camino.nuevo_paso(indice_paso)
                nuevos_caminos.append(camino)
        fin = time.time()
        set_caminos_finales = set(nuevos_caminos)
        fin_con_copia = time.time()
        print("set caminos ", len(set_caminos_finales) ,"caminos borrados ", len(nuevos_caminos) - len(set_caminos_finales))
        tiempo_transcurrido = fin - inicio
        tiempo_transcurrido_con_copia = fin_con_copia - fin
        print(f"Tiempo en paso {indice_fila} : {tiempo_transcurrido} segundos {tiempo_transcurrido_con_copia}")
    print("caminos totales ", len(set_caminos_finales))