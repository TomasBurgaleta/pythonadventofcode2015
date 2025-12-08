class Camino:

    def __init__(self, ruta):
        self._ruta = ruta

    def __eq__(self, otro):
        if not isinstance(otro, Camino):
            return False
        return self._ruta == otro.ruta

    def __hash__(self):
        return hash(tuple(self._ruta))

    def __str__(self):
        return f"Camino{self._ruta}"

    def nuevo_paso(self,nueva_valor):
        self._ruta.append(nueva_valor)

    @property
    def ruta(self):
        return self._ruta

    @ruta.setter
    def ruta(self, ruta):
        self._ruta = ruta