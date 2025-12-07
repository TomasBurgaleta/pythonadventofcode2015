class Bateria:

    def __init__(self, banco, chispazos):
        self.banco = int (banco)
        self.chispazos = chispazos


    @property
    def banco(self):
        return self._banco

    @banco.setter
    def banco(self, banco):
        self._banco = banco

    @property
    def chispazos(self):
        return self._chispazos

    @chispazos.setter
    def chispazos(self, chispazos):
        self._chispazos = chispazos