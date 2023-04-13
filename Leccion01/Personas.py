class Persona:
    # metodo para agregar atributos de objetas o de
    # intancia __init__(self) dunder
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre # self.nombre es un atributo
        self.apellido = apellido # nombre es un parametro
        self.edad = edad


persona1 = Persona('Juan', 'Perez', 28) #se llama de manera indirecta a init
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Karla', 'Gomez', 30)
print(f'Objeto persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

# Modificar los valores de un objeto

persona1.nombre = 'Juan Carlos' # no es recomendable ser directo
persona1.apellido = 'Juarez'
persona1.edad = 25
print(f'Objeto persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')


