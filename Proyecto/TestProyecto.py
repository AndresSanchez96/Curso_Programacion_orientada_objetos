from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('Acer', 'USB')
monitor1 = Monitor('Asus', 21)
computadora1 = Computadora('Acer', monitor1, teclado1, raton1)


teclado2 = Teclado('HP', 'USB')
raton2 = Raton('Acer', 'Bluetooth')
monitor2 = Monitor('Asus', 21)
computadora2 = Computadora('Asus', monitor1, teclado1, raton1)

teclado3 = Teclado('Gamer', 'Bluetooth')
raton3 = Raton('Gamer', 'Bluetooth')
monitor3 = Monitor('Asus', 32)
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]

orden1 = Orden(computadoras1)
#print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)
