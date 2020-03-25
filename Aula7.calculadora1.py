class calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicação(self):
        return self.valor_a * self.valor_b

    def divisão(self):
        return self.valor_a / self.valor_b


calculadora = calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicação())
print(calculadora.divisão())

