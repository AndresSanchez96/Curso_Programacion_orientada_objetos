from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

#No se puede instanciar una clase abstracta
#figura = FiguraGeometrica()

print('Creacion objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5,'Rojo')
print(f'Calculo area cuadrado: {cuadrado1.CalcularArea()}')
print(cuadrado1)

#MRO Method Resolution Order
#print(Cuadrado.mro())

print('Creacion objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(10,5,'Rojo')
print(f'Calculo area rectangulo: {rectangulo1.CalcularArea()}')
print((rectangulo1))