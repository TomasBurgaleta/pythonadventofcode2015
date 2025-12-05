from Rango import Rango

class LectorRangos:

    def __init__(self, rangoInicial):
        self.rangoInicial = rangoInicial


    def __rellenaFin(self, longCifra):
        return (10 ** (longCifra)) - 1

    def __rellenaInicio(self, longCifra):
        return (10 ** (longCifra ))

    def rangosAVerificar(self,rangoInicial):
        rangoList = []
        longIni = len(str(rangoInicial.inicio))
        longFinal = len(str(rangoInicial.fin))
        inicio = rangoInicial.inicio
        fin = rangoInicial.fin

        for i in range(longIni, longFinal + 1):
            if i < longFinal :
                rangoList.append(Rango(inicio, self.__rellenaFin(i)))
                inicio = self.__rellenaInicio(i)
            else:
                rangoList.append(Rango(inicio, fin))
        return rangoList


    def idNoValidosPor2Veces(self, rangoList):
        suma = 0
        idsNulos = []

        for rango in rangoList:
            longIni = len(str(rango.inicio))
            longFinal = len(str(rango.fin))
            if (longIni == longFinal) and longIni%2  == 0:
                mitadIni = str(rango.inicio)[:longIni//2]
                mitadFin = str(rango.fin)[:longIni//2]
                for num in range(int(mitadIni), int(mitadFin) + 1):
                    numStr = str(num) + str(num)
                    if(int(numStr) >= rango.inicio and int(numStr) <= rango.fin):
                        #idsNulos.append(int(numStr))
                        suma = suma + int(numStr)
        return suma

    def construyeNumero(self, numero, repeticionesPatron):
        salida = str(numero)
        for num in range(1, repeticionesPatron):
            salida = salida + str(numero)
        return int(salida)

    def idNoValidosPorNVeces(self, rangoList):
        suma = 0

        idsNulos = []

        for rango in rangoList:
            maxRepeticioes = len(str(rango.inicio)) // 2
            longIni = len(str(rango.inicio))
            longFinal = len(str(rango.fin))
            numerosYaSumados = []
            for factorRepeticion in range(1, maxRepeticioes + 1):
                if (longIni == longFinal) and longIni%factorRepeticion  == 0: # pra ver que puede tener espejo multiple d erepeticiones
                    repeticionesEnBucle = longIni//factorRepeticion
                    mitadIni = str(rango.inicio)[:factorRepeticion]
                    mitadFin = str(rango.fin)[:factorRepeticion]
                    for num in range(int(mitadIni), int(mitadFin) + 1):
                        numStr = self.construyeNumero(num,repeticionesEnBucle)
                        if(int(numStr) >= rango.inicio and int(numStr) <= rango.fin):
                            #idsNulos.append(int(numStr))
                            if not(numStr in numerosYaSumados):
                                print(int(numStr))
                                suma = suma + int(numStr)
                                numerosYaSumados.append(int(numStr))
        return suma





