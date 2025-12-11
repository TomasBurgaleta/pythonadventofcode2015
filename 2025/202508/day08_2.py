from pyasn1_modules.rfc4357 import id_GostR3410_94

from Caja import Caja
from Circuito import Circuito
import copy

cajas = []
circuitos = []
cajas_a_remover = []
conexiones_ya_puestas = []
mapa_conexiones = {}

ultima_conexion = None

def poner_en_circuito(caja_inicial, caja_minima_distancia):
    for indice_circuitos in range(0, len(circuitos)):
        circuito = circuitos[indice_circuitos]
        if circuito.contain(caja_inicial) and circuito.contain(caja_minima_distancia):
            print("añadiendo al circuito una conexion si añadir nuevas cajas")
            circuito.crear_conexion(caja_inicial, caja_minima_distancia)
            #circuito.poner_nueva_caja(caja_minima_distancia)
            # cajas_a_remover.remove(caja_minima_distancia)
            print("circuito final", circuito)
            conexiones_ya_puestas.append([caja_inicial, caja_minima_distancia])
            conexiones_ya_puestas.append([caja_minima_distancia, caja_inicial])
            return
        elif circuito.contain(caja_inicial) and not (circuito.contain(caja_minima_distancia)):
            if not(caja_minima_distancia in cajas_a_remover) :
                fusionar_circuitos(circuito, caja_minima_distancia, caja_inicial)
            else:
                print("añadiendo a circuito ya creado (a) la caja", caja_minima_distancia)
                circuito.crear_conexion(caja_inicial, caja_minima_distancia)
                circuito.poner_nueva_caja(caja_minima_distancia)
                print("circuito ", circuito)
                cajas_a_remover.remove(caja_minima_distancia)
                print("cajas a remover", len(cajas_a_remover))
            conexiones_ya_puestas.append([caja_inicial, caja_minima_distancia])
            conexiones_ya_puestas.append([caja_minima_distancia, caja_inicial])
            return
        elif circuito.contain(caja_minima_distancia) and not (circuito.contain(caja_inicial)):
            if not(caja_inicial in cajas_a_remover) :
                fusionar_circuitos(circuito, caja_inicial, caja_minima_distancia)
            else :
                print("añadiendo a circuito ya creado (b) la caja", caja_inicial)
                circuito.crear_conexion(caja_inicial, caja_minima_distancia)
                circuito.poner_nueva_caja(caja_inicial)
                print("circuito ", circuito)
                cajas_a_remover.remove(caja_inicial)
                print("cajas a remover", len(cajas_a_remover))
            conexiones_ya_puestas.append([caja_inicial, caja_minima_distancia])
            conexiones_ya_puestas.append([caja_minima_distancia, caja_inicial])
            return

def fusionar_circuitos(circuito_a, caja_en_otro_circuito, caja_circuito_a):
    print("circuitos a fusionar", caja_en_otro_circuito, caja_circuito_a, "para el circuito a", circuito_a)
    for indice_circuitos in range(0, len(circuitos)):
        circuito_b = circuitos[indice_circuitos]
        if not(circuito_b == circuito_a) and circuito_b.contain(caja_en_otro_circuito) :
            print("circuitos a fusionarse", circuito_a, circuito_b)
            cajas_circuito_b = circuito_b.lista_cajas
            conexiones_circuito_b = circuito_b.lista_conexiones
            for caja in cajas_circuito_b:
                print("añadiendo caja a circuito ya creado", caja)
                circuito_a.poner_nueva_caja(caja)
            for conex in conexiones_circuito_b:
                print("añadiendo conexion a circuito ya creado", conex)
                circuito_a.poner_conexion(conex)
            print("circuito ", circuito_a)
            circuitos.remove(circuito_b)
            circuito_a.crear_conexion(caja_circuito_a, caja_en_otro_circuito)
            return

# def crear_conexion():
#     distancia_minima = None
#     caja_inicial = None
#     caja_minima_distancia = None
#     for indice_caja_i in range(0, len(cajas)):
#         caja_i = cajas[indice_caja_i]
#         for indice_caja_j in range(0, len(cajas)):
#             caja_j = cajas[indice_caja_j]
#             nueva_conexion = [caja_i, caja_j]
#             if not (caja_i == caja_j) and not(nueva_conexion in conexiones_ya_puestas):
#                 distancia = caja_i.distancia(caja_j)
#                 if (distancia_minima == None or distancia_minima > distancia):
#                     distancia_minima = distancia
#                     caja_inicial = caja_i
#                     caja_minima_distancia = caja_j
#
#     if (caja_inicial in cajas_a_remover) and (caja_minima_distancia in cajas_a_remover) :
#         circuito_nuevo = Circuito(caja_inicial, caja_minima_distancia)
#         print("creado nuevo circuito ", caja_inicial, caja_minima_distancia)
#         print("circuito ", circuito_nuevo)
#         circuitos.append(circuito_nuevo)
#         cajas_a_remover.remove(caja_minima_distancia)
#         cajas_a_remover.remove(caja_inicial)
#         print("cajas a remover", len(cajas_a_remover))
#         conexiones_ya_puestas.append([caja_inicial,caja_minima_distancia])
#         conexiones_ya_puestas.append([caja_minima_distancia, caja_inicial])
#     else :
#         poner_en_circuito(caja_inicial, caja_minima_distancia)
#

def crear_conexion(id_conexion):
    id_cajas = id_conexion.split('_')
    id_0 = id_cajas[0]
    id_1 = id_cajas[1]
    coordenadas_0 = (id_cajas[0]).split('.')
    coordenadas_1= (id_cajas[1]).split('.')
    caja_inicial = Caja(coordenadas_0[0], coordenadas_0[1],coordenadas_0[2])
    caja_minima_distancia = Caja(coordenadas_1[0], coordenadas_1[1],coordenadas_1[2])

    if (caja_inicial in cajas_a_remover) and (caja_minima_distancia in cajas_a_remover) :
        circuito_nuevo = Circuito(caja_inicial, caja_minima_distancia)
        print("creado nuevo circuito ", caja_inicial, caja_minima_distancia)
        print("circuito ", circuito_nuevo)
        circuitos.append(circuito_nuevo)
        cajas_a_remover.remove(caja_minima_distancia)
        cajas_a_remover.remove(caja_inicial)
        print("cajas a remover", len(cajas_a_remover))
        conexiones_ya_puestas.append([caja_inicial,caja_minima_distancia])
        conexiones_ya_puestas.append([caja_minima_distancia, caja_inicial])
    else :
        poner_en_circuito(caja_inicial, caja_minima_distancia)





def crear_mapa_conexiones():
    distancia_minima = None
    caja_inicial = None
    caja_minima_distancia = None
    for indice_caja_i in range(0, len(cajas)):
        caja_i = cajas[indice_caja_i]
        for indice_caja_j in range(0, len(cajas)):
            caja_j = cajas[indice_caja_j]
            nueva_conexion = [caja_i, caja_j]
            if not (caja_i == caja_j):
                distancia = caja_i.distancia(caja_j)
                key1 = caja_i.id_caja() + "_" + caja_j.id_caja()
                #key2 = caja_j.id_caja() + "_" + caja_i.id_caja()
                mapa_conexiones[key1] = distancia
                #mapa_conexiones[key2] = distancia

def ordenar_mapa_conexiones():
    lista_ordenada_por_valor = sorted(
        mapa_conexiones.items(),
        key=lambda item: item[1]  # item[1] es el valor (la temperatura)
    )
    return lista_ordenada_por_valor

def ordena_circuitos():
    lista_ordenada = sorted(circuitos, key=lambda circuito: len(circuito.lista_cajas))
    return lista_ordenada


with open("data01.txt", "r") as archivo:
#with open("example.txt", "r") as archivo:

    filas = [x.strip() for x in archivo.readlines()]

    #creacion de cajas
    for fila in filas:
        coordenadas = fila.split(',')
        caja = Caja(coordenadas[0], coordenadas[1],coordenadas[2])
        cajas.append(caja)
    print(len(cajas))
    print(len(circuitos))
    cajas_a_remover = copy.deepcopy(cajas)

    #creacion de conexiones
    crear_mapa_conexiones()
    paso = 0
    lista_ordenada_por_valor = ordenar_mapa_conexiones()
    par_conexion = None

    for paso in range (0 ,100000):
        par_conexion = lista_ordenada_por_valor[paso*2]
        print()
        print("paso ",paso)
        crear_conexion(par_conexion[0])
        if(len(cajas_a_remover) == 0 and len(circuitos) == 1):
            print("ultima conexion ", par_conexion[0])
            break




