class Persona:
    # metodo para agregar atributos de objetas o de
    # intancia __init__(self) dunder
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        # *arg son para tuplas y **kwargs son para diccionarios
        self.nombre = nombre # self.nombre es un atributo
        self.apellido = apellido # nombre es un parametro
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    #metodos de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1 = Persona('Juan', 'Perez', 28, '3183357183' ,3 ,3, 4, m = 'Manzana', p ='Pera') #se llama de manera indirecta a init
persona1.mostrar_detalle()

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()