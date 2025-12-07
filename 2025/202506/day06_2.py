import numpy as np
import re

from pandas.core.dtypes.inference import is_decimal


def construir_nuevo_valor_desde_derecha(valores, indice):
    nuevo_valor = ""
    for indiceValor in range (0,len(valores) - 1) :
        valor_cadena =valores[indiceValor]
        longitud = len(valor_cadena)
        if longitud > indice:
            nuevo_numero = valor_cadena[longitud - 1 - indice]
            nuevo_valor += nuevo_numero
    return nuevo_valor

def construir_nuevo_valor_desde_izquierda(valores, indice):
    nuevo_valor = ""
    for indiceValor in range(0, len(valores) - 1):
        valor_cadena = valores[indiceValor]

        longitud = len(valor_cadena)
        if longitud > indice:
            nuevo_numero = valor_cadena[indice]
            nuevo_valor += nuevo_numero
    return nuevo_valor


def tam_max_valores(valores):
    max = 0
    for valor in valores:
        valor_cadena = str(valor).split('.')[0]
        longitud = len(valor_cadena)
        if longitud > max:
            max = longitud
    return max


def construir_array_nuevos_valores(valores, derecha):
    tam_max = tam_max_valores(valores)
    nuevos_valores = []
    for indice in range (0 ,tam_max):
        if derecha :
            nueva_cadena = construir_nuevo_valor_desde_derecha(valores, indice)
        else:
            nueva_cadena = construir_nuevo_valor_desde_izquierda(valores, indice)
        if nueva_cadena.strip().isdigit():
            nuevos_valores.append(int(nueva_cadena))
    return nuevos_valores

def suma_valores_pulpo(valores, derecha):
    nuevos_valores = construir_array_nuevos_valores(valores, derecha)
    resultado = 0
    for valor in nuevos_valores:
        resultado += int(valor)
    print("suma :valores antiguos ", valores, " nuevos valores ", nuevos_valores, " resultado: ", resultado)
    return resultado

def multiplicacion_valores_pulpo(valores, derecha):
    nuevos_valores = construir_array_nuevos_valores(valores, derecha)
    resultado = 1
    for valor in nuevos_valores:
        resultado *= int(valor)
    print("multiplicacion :valores antiguos ", valores, " nuevos valores ", nuevos_valores, " resultado: ", resultado)
    return resultado


def lectura_datos(filas):
    ultima_fila = len(filas)
    lista_inicio_valores = []
    indice = 0
    delimitadores = r"[+*]"
    lista_resultado = re.split(delimitadores, filas[ultima_fila -1])
    lista_espacios_en_blanco = [len(espacios) for espacios in lista_resultado]
    correcion = 0
    for tam_espacios in lista_espacios_en_blanco:
        indice += tam_espacios + correcion
        correcion = 1
        lista_inicio_valores.append(indice)
        print(lista_inicio_valores)
    return  lista_inicio_valores

def crear_columnas(filas, lista_inicio_valores, total_columnas):
    numFilas = len(filas)
    columnas =[]
    for indice_columna in range (0, total_columnas - 1):
        columna = []
        for indice_fila in range (0, numFilas):
            fila = filas[indice_fila]
            valor = fila[lista_inicio_valores[indice_columna]: lista_inicio_valores[indice_columna +1]]
            columna.append(valor)
        columnas.append(columna)
    columna = []
    for indice_fila in range(0, numFilas):
            tam_fila = len(filas[indice_fila])
            fila = filas[indice_fila]
            columna.append(fila[lista_inicio_valores[total_columnas - 1]: tam_fila].strip())
    columnas.append(columna)
    return columnas

def es_lectura_izquierda(columna):
    for valor in columna:
        if valor[0] == " ":
            return False
    return True

def es_operador_suma(columa):
    operador = columa[len(columa) - 1]
    if "+" in operador :
        return True
    return False

#with open("example.txt", "r") as archivo:
with open("data01.txt", "r") as archivo:
    filas = [x for x in archivo.readlines()]
    lista_inicio_valores = lectura_datos(filas)
    total_columnas = len(lista_inicio_valores) -1
    columnas = crear_columnas(filas, lista_inicio_valores, total_columnas)

    sumando = 0
    for columna in columnas:
        es_suma = es_operador_suma(columna)
        es_izquierda = es_lectura_izquierda(columna)

        if es_suma :
            suma = suma_valores_pulpo(columna, not(es_izquierda))
        else :
            suma = multiplicacion_valores_pulpo(columna, not(es_izquierda))
        sumando += suma

    print(sumando)





