class Persona:
    # metodo para agregar atributos de objetas o de
    # intancia __init__(self) dunder
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre # self.nombre es un atributo
        self.apellido = apellido # nombre es un parametro
        self.edad = edad

    #metodos de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28) #se llama de manera indirecta a init
persona1.mostrar_detalle()
persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()