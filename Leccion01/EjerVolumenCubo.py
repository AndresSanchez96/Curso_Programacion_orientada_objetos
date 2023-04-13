class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    #Metodo de instancia
    def volumen(self):
        return self.alto * self.ancho * self.profundidad

ancho = int(input('Digite el ancho del cubo: '))
alto = int(input('Digite el alto del cubo. '))
profundidad = int(input('Digite la profundidad del cubo: '))

volumen = Cubo(ancho,alto,profundidad)
print(f'El volumen del cubo es: {volumen.volumen()} m3')