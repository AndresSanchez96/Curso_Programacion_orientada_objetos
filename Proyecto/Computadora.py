from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''

if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('Acer', 'USB')
    monitor1 = Monitor('Asus', 21)
    computadora1 = Computadora('Acer', monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado('HP', 'USB')
    raton2 = Raton('Acer', 'Bluetooth')
    monitor2 = Monitor('Asus', 21)
    computadora2 = Computadora('Asus', monitor1, teclado1, raton1)
    print(computadora2)