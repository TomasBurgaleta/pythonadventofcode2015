from Rango import Rango
from LectorRangos import LectorRangos

with open("data01.txt", "r") as fichero:
#with open("example.txt", "r") as fichero:
    suma = 0
    for linea in fichero:
         grupoRangos = linea.strip().split(",")
         rangoList = []
         for rangos in grupoRangos:
             rangoLeido = rangos.split("-")
             rangoList.append(Rango(rangoLeido[0], rangoLeido[1]))
         for rangoLectura in rangoList:
             lector = LectorRangos(rangoLectura)
             rangosValidos = lector.rangosAVerificar(rangoLectura)
             print(str(rangoLectura) + " se transforma en " + str(rangosValidos))
             #idsNoValidos = lector.idNoValidos(rangosValidos)
             suma = suma + lector.idNoValidosPorNVeces(rangosValidos)
             #print("ids nulos para sacar: " + str(idsNoValidos))
    print(suma)


