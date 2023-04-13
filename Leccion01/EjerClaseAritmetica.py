class Aritmetica:
    """
    Clase Aritmetica para realizar las operaciones
    + - * etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Metodos de intancia 
    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicacion(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

aritemetica1 = Aritmetica(5,3)
print(f'La suma es: {aritemetica1.sumar()}')
print((f'La resta es: {aritemetica1.restar()}'))
print((f'La multiplicacion es: {aritemetica1.multiplicacion()}'))
print((f'La division es: {aritemetica1.dividir():.2f}'))