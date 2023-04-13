##HERENCIA

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: \n  Nombre: {self.nombre}, \n  edad: {self.edad}'

class Empleado(Persona): #clase hija
    def __init__(self, nombre,edad,sueldo):
        super().__init__(nombre,edad) #metodo para acceder a la clase padre
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} \n  Sueldo: {self.sueldo}'