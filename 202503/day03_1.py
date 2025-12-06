from Bateria import Bateria



def buscar_chispazo(bateria, indice_max_busqueda):

    numerosBanco = [int(digito) for digito in str(bateria.banco)]
    for digito in range(9, -1, -1):
        indice = buscar_numero_en_cadena(numerosBanco, digito, indice_max_busqueda)
        if indice > -1 :
            return extraer_digito_bateria(bateria, digito, indice)
    return bateria

def buscar_numero_en_cadena(cadena, numero, indice_max_busqueda):
    if numero in cadena:
        indice = cadena.index(numero)
        if indice < indice_max_busqueda:
            return indice
    return -1

def extraer_digito_bateria(bateria, numero, indice) :
    bancoFinal = ""
    numerosBanco = [str(x) for x in str(bateria.banco)]
    for digito_banco in range (0, len(str(bateria.banco))):
        if digito_banco > indice :
            bancoFinal += numerosBanco[digito_banco]
    chispazo_acumulado =  str(bateria.chispazos) + str(numero)
    if bancoFinal == "":
        bancoFinal = 0
    return Bateria(bancoFinal, chispazo_acumulado)

suma_chispazos= 0
with open("data01.txt", "r") as archivo:
#with open("example.txt", "r") as archivo:
    bancos = [x.strip() for x in archivo.readlines()]
    baterias = []
    for banco in bancos:
        baterias.append(Bateria(str(banco), ""))

    for bateria in baterias:
        for busqueda in range(1,3):
            indice_max_busqueda = len(str(bateria.banco)) - 2
            bateria = buscar_chispazo(bateria, indice_max_busqueda + busqueda)
        
        chispazos = int(bateria.chispazos)
        print(chispazos)
        suma_chispazos  += chispazos
    print(suma_chispazos)


#17324


