from operator import truediv


class Rango:

    def __init__(self, inicio, fin):
        self.inicio = int (inicio)
        self.fin = int (fin)

    @property
    def inicio(self):
        return self._inicio

    @inicio.setter
    def inicio(self, inicio):
        self._inicio = inicio

    @property
    def fin(self):
        return self._fin

    @fin.setter
    def fin(self, fin):
        self._fin = fin

    def mostrar_rango(self):
        print(f"inicio: {self.inicio}, fin: {self.fin}")

    def __repr__(self):
        # Devuelve una cadena de texto que describe el objeto
        return f"Rango(inicio={self.inicio}, fin={self.fin})"


    def isValidToCheck(self):
        longIni = len(self.inicio)
        longFinal = len(self.inicio)
        if longIni%2 == 0 and longFinal%2 == 0 :
            return True
        else:
            return False