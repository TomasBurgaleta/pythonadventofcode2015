import numpy as np

max_rollos_prox = 4
contador = 0
def contar_rollos_proximos(matriz, fila, columna, max_filas, max_columna):
    suma_roolos_adyacentes = 0
    for indice_fila_busqueda in range(-1, 2):
        for indice_columna_busqueda in range(-1, 2):
            nueva_fila = fila + indice_fila_busqueda
            nueva_columna = columna + indice_columna_busqueda
            if nueva_fila >= 0 and nueva_columna >= 0 and nueva_fila < max_filas and nueva_columna < max_columna:
                valor_matriz = int (matriz[nueva_fila, nueva_columna])
                if valor_matriz == 1 :
                    suma_roolos_adyacentes += 1
    return suma_roolos_adyacentes

with open("data01.txt", "r") as archivo:
#with open("example.txt", "r") as archivo:
    filas_rollos = [x.strip() for x in archivo.readlines()]

    long_columnas = len(filas_rollos[0])
    long_filas = len(filas_rollos)
    indice_x = int(0)
    indice_y = int(0)
    print(long_columnas)
    print(long_filas)
    matriz = np.zeros((long_filas, long_columnas))
    for filas in filas_rollos:
        indice_y = int(0)
        for columna in filas:
            if columna == "@":
                matriz[indice_x,indice_y] = 1
            indice_y = indice_y + 1
        indice_x = indice_x + 1

    print(matriz)
    condicion = matriz > 0

    # 2. Obtener y mostrar los valores directamente
    indices_filas, indices_columnas = np.where(condicion)
    for fila, columna in zip(indices_filas, indices_columnas):
        # Obtenemos el valor usando los índices
        valor = matriz[fila, columna]
        num_rollos_proximos = contar_rollos_proximos(matriz, fila, columna, long_filas, long_columnas)
        #print(f"El valor {valor} se encuentra en la posición [{fila}, {columna}]")
        if(num_rollos_proximos <= max_rollos_prox):
            contador  += 1

    print(contador)