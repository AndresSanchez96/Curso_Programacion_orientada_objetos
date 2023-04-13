# clase hija

from HerenciaMultiple import FiguraGeomtreca
from Color import Color

class Cuadrado(FiguraGeomtreca, Color):
    def __init__(self, lado, color):
        FiguraGeomtreca.__init__(self, lado, lado) #Inicializa clase padre mas general
        Color.__init__(self, color)
    def CalcularArea(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeomtreca.__str__(self)} {Color.__str__(self)}'