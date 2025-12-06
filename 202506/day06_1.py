import numpy as np


def suma_valores(valores):
    resultado = 0
    for valor in valores:
        resultado += int(valor)
    return resultado


def multiplicacion_valores(valores):
    resultado = 1
    for valor in valores:
        resultado *= int(valor)
    return resultado

#with open("example.txt", "r") as archivo:
with open("data01.txt", "r") as archivo:
    filas = [x.strip() for x in archivo.readlines()]
    longitud_numeros = [int(x) for x in filas[0].strip().split()]
    rango_numeros = int(len(filas) - 1)
    fila_operadores = filas[len(filas) - 1].strip().split()

    matriz = np.zeros((int(len(longitud_numeros)),  rango_numeros))
    for numFila in range(0, rango_numeros):
        cadena_numero = filas[numFila].strip()
        numeros = [int(x) for x in cadena_numero.split()]
        matriz[:, numFila] = numeros

    sumando = 0
    for indice in range (0, rango_numeros):
        valores_fila = matriz[indice,:]
        operador = fila_operadores[indice]
        if operador == "+":
            suma = suma_valores(valores_fila)
        else:
            suma = multiplicacion_valores(valores_fila)
        sumando += suma

    print(sumando)





