

rangos = []
productos = []
valores_validos = []
contador_valores_validos = 0


def verificar_producto(rangos, producto):
    for rango in rangos:
        valores_rango = rango.split("-")
        inicio = int(valores_rango[0])
        fin = int(valores_rango[1])
        if (producto >= inicio and producto <= fin):
            return int(1)
    return int(0)


#with open("example.txt", "r") as archivo:
with open("data01.txt", "r") as archivo:
    filas = [x.strip() for x in archivo.readlines()]
    for fila in filas:
        if  "-" in fila:
            rangos.append(fila)
        else:
            if fila.isdigit():
                productos.append(fila)
    print(len(rangos))
    print(len(productos))
#añadimos los valores validos en un list

    for producto in productos:
        contador_valores_validos  = contador_valores_validos + verificar_producto(rangos, int(producto))

    print(contador_valores_validos)