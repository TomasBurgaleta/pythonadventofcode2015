class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        self._x = valor

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, valor):
        self._y = valor

    def __eq__(self, otro):
        """Compara si dos puntos son iguales"""
        return self.x == otro.x and self.y == otro.y

    def __hash__(self):
        """Genera un hash del punto para usar en sets o dicts"""
        return hash((self.x, self.y))

    def __str__(self):
        """Representación en string"""
        return f"Point({self.x}, {self.y})"

