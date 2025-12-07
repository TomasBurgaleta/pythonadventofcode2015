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
             suma = suma + lector.idNoValidosPor2Veces(rangosValidos)
             #print("ids nulos para sacar: " + str(idsNoValidos))
    print(suma)
#23039913998


#leer los rangos de los registros
#añadirlo a un ojetos que se llame rango_registros
#comprobar si parte del registro tiene digitos pares
#verificar el rango de inicio a fin en el que son pares
#buscar la mitad de los digitos pares, dobarlo y verificar si estan dentro de ese rango
#sumar el total de ids no validos