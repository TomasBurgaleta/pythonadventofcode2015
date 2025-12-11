import math
from InterfazDistancia import InterfazDistancia

class Caja(InterfazDistancia):


    def __init__(self, x, y, z):
        # super().__init__() # No es estrictamente necesario si InterfazDistancia no hace nada
        self._x = int(x)
        self._y = int(y)
        self._z = int(z)
        self.mapa_distacias = {}

    # 1. Mover los getters a nivel de clase
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def __str__(self):
        """Devuelve una representación legible de la caja."""
        return f"Caja(x={self._x}, y={self._y}, z={self._z})"

    # 2. Mover la implementación de distancia a nivel de clase
    def distancia(self, caja2):
        # 3. Usar el nombre de la clase para acceder a la caché
        distancia = self.mapa_distacias.get(caja2)

        if distancia is None:  # Forma pythónica de chequear None

            delta_x_cuadrado = (caja2.x - self.x) ** 2
            delta_y_cuadrado = (caja2.y - self.y) ** 2
            delta_z_cuadrado = (caja2.z - self.z) ** 2
            suma_cuadrados = delta_x_cuadrado + delta_y_cuadrado + delta_z_cuadrado
            distancia = math.sqrt(suma_cuadrados)
            self.mapa_distacias[caja2] = distancia

        return distancia

    def id_caja(self):
        return f"{self._x}.{self._y}.{self._z}"

    # Los métodos __eq__ y __hash__ son correctos para usar la instancia como clave de diccionario
    def __eq__(self, __value):
        if not isinstance(__value, Caja):
            return NotImplemented

        return self._x == __value._x and self._y == __value._y and self._z == __value._z

    def __hash__(self):
        # Usar una tupla o hash() para una función hash más robusta
        return hash((self._x, self._y, self._z))

