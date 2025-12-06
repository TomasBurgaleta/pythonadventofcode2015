from Rango import Rango
#with open("data01.txt", "r") as archivo:

rangos_iniciales = []
rangos_finales = []
productos = []
valores_validos = []
contador_valores_validos = 0


# def sumar_producto_rango(rangos, producto):
#     for rango in rangos:
#         valores_rango = rango.split("-")
#         inicio = int(valores_rango[0])
#         fin = int(valores_rango[1])
#         total = fin - inicio +1
#     return int(0)

def annadir_rango(rangos_finales, rango) :
    for rango_ya_añadido in rangos_finales:
        print("verificamos " , rango, "con el rango guardado ", rango_ya_añadido)
        if rango_ya_añadido.es_valor_en_rango(rango.inicio):
            rango.inicio = rango_ya_añadido.fin + 1
            print("rango modificado ", rango)
            if not(rango.es_rango_valido()) :
                print("no valido " , rango)
                print(rango)
                return
        if rango_ya_añadido.es_valor_en_rango(rango.fin):
            rango.fin = rango_ya_añadido.inicio - 1
            print("rango modificado ", rango)
            if not(rango.es_rango_valido()) :
                print("no valido " , rango)
                print(rango)
                return
    print("rango guardado ", rango)
    rangos_finales.append(rango)


#with open("example.txt", "r") as archivo:
with open("data01.txt", "r") as archivo:
    filas = [x.strip() for x in archivo.readlines()]
    for fila in filas:
        if  "-" in fila:
            valores_rango = fila.split("-")
            rangos_iniciales.append(Rango(int(valores_rango[0]),int(valores_rango[1])))

    productos_ordenados = sorted(rangos_iniciales, key=lambda p: p.total_valores(), reverse=True)
    for rangos_a_colocar in productos_ordenados:
        annadir_rango(rangos_finales, rangos_a_colocar)

    for rangos_sumar in rangos_finales:
        #print(rangos_sumar.total_valores())
        contador_valores_validos += rangos_sumar.total_valores()
        print(contador_valores_validos, " sumamos ", rangos_sumar.total_valores())

    print(contador_valores_validos)
