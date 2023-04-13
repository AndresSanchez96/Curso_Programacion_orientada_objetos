class Rectangulo:
    def __init__(self,Altura, Base):
        self.Altura = Altura
        self.Base = Base
    #Metedo de instancia
    def Area(self):
        return self.Altura * self.Base

print('Area de un rectangulo')
altura = int(input('Digite la altura del rectangulo: '))
base = int(input('Digite la base del rectangulo: '))

area = Rectangulo(altura, base)
print(f'La area del rectangulo es: {area.Area()}')