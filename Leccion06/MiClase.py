class MiClase:

    variables_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    #Metodo estatico
    @staticmethod
    def metodo_estatico():
        print(MiClase.variables_clase,'Metodo estatico')

    #Metodos de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variables_clase,'Metodo de clase')

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()

MiClase.metodo_clase()
miObjeto1 = MiClase('Variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

MiClase.metodo_estatico()
""""
Para variables de clase no es necesario crear un objeto para ser llamado
caso contrario a las variables de instancia incluidads en __init__
desde el objeto tambien podemos llamar a la vriable de clase
"""

print(MiClase.variables_clase)
miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variables_clase)

MiClase.variables_clase2 = 'Valor variable clase 2' # se puede crear variables de clase por fuera
print(MiClase.variables_clase2)
print(miClase.variables_clase2)

