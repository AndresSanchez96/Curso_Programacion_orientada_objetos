from Encapsulamiento import Persona

print('Creaccion objetos'.center(50,'-')) #center para centrar  con 50 objetos de -
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminacion de objetos'.center(50,'-'))
del persona1

# para mostrar mas detalle se creara metodo destructor en Encapsulamiento
