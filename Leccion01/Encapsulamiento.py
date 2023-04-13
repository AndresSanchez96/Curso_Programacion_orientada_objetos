class Persona:
    # metodo para agregar atributos de objetas o de
    # intancia __init__(self) dunder
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre # self.nombre es un atributo el _ atributo encapsulado
                              # sirve para no llamar directamente
        self._apellido = apellido # nombre es un parametro
        self._edad = edad
    # Metodos GET para recuperar, obtener y SET para modificar
    #decorador
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter #Modificar
    def nombre(self, nombre):
        self._nombre = nombre

    #metodos de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

    def __del__(self): #metodo destructor
        print(f'Persona: {self._nombre} {self._apellido}')

if __name__ == '__main__': ## este if sirve para que en el momento de que otros modulos
                          ## llamen a este modulo no se imprima lo siguiente
    persona1 = Persona('Juan', 'Perez', 28)  # se llama de manera indirecta a init
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Lara'
    persona1.edad = 30
    persona1.mostrar_detalle()

    print(__name__)
