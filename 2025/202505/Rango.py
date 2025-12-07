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

    # def __repr__(self):
    #     # Devuelve una cadena de texto que describe el objeto
    #     return f"Rango(inicio={self.inicio}, fin={self.fin} , total={self.total_valores()})"

    def __str__(self):
        return f"Rango(inicio={self.inicio}, fin={self.fin} , total={self.total_valores()})"

    def es_valor_en_rango(self, valor):
        if self.inicio <= valor and self.fin >= valor:
            return True

    def es_rango_valido(self):
        if self.inicio <= self.fin :
            return True
        else:
            return False

    def total_valores(self):
        return self.fin - self.inicio + 1