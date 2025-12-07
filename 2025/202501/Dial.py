class Dial:

    maxValue = 100

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, valor):
        self._x = valor


    def __str__(self):
        return f"Dial({self.x})"

    def rotation(self, turnRight, value):

        if turnRight:
            self.x = self.x + value
        else:
            self.x = self.x - value

        if self.maxValue <= abs(self.x):
            self.x = self.x%100
        if self.x < 0:
            self.x = self.x + 100

        return self.x

    # algoritmo poco elegante
    # def rotationWithClick(self, turnRight, value):
    #     numClicks = 0
    #     numClicks = numClicks + abs((value // 100))
    #     value = value % 100
    #     if turnRight:
    #         self.x = self.x + value
    #         if self.maxValue <= abs(self.x):
    #             self.x = self.x % 100
    #             if  self.x != 0:
    #                 numClicks = numClicks + 1
    #     else:
    #         if self.x == 0:
    #             self.x = self.x - value + 100
    #         else:
    #             self.x = self.x - value
    #             if self.x < 0:
    #                 self.x = self.x + 100
    #                 numClicks = numClicks + 1
    #     return numClicks


    def rotationWithClick(self, turnRight, value):
        # clicks iniciales
        numClicks = abs((value // 100))
        startPosition = self.x
        finalPosition = self.rotation(turnRight, value)

        resto = startPosition - finalPosition

        if startPosition == finalPosition :
            return numClicks # como ha dado 1 o n  vueltas completas estas ya estas contabilizadas y no hay que sumar mas
        if finalPosition == 0 : # como esta en el dial 0 no se suma nada mas en este metodo ya el 0 se suma externamente
            return numClicks
        if turnRight and (finalPosition < startPosition) : # le falta un paso por el 0 para sumar
            return numClicks + 1
        if not turnRight and startPosition > 0 and  (finalPosition > startPosition) :
            return numClicks + 1

        return numClicks