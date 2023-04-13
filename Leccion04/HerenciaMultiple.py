#FIGURA GEOMETRICA
#Clse padre
# ABS = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeomtreca(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):      # Validaciones
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor Erroneo de ancho {ancho}')
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo de alto {alto}')

    # Encapsulamiento

    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):  #Validaciones para modificaciones
            self._ancho = ancho
        else:
            print(f'Valor erroneo de ancho {ancho}')

    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo de alto {alto}')

    @abstractmethod # con el metodo abstracto se oblica a las clases hijas a implementar calcular area
    def CalcularArea(self):
        pass

    def __str__(self):
        return f'Figura Geometrica [Ancho: {self._ancho} Largo: {self._alto}'

    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False