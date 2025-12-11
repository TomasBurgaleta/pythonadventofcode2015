from abc import ABC, abstractmethod

class InterfazDistancia(ABC):

    def __init__(self):
        # Inicialización base, si es necesaria
        pass

    @abstractmethod
    def distancia(self, caja):
        pass