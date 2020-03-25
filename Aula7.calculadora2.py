class calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicação(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisão(self, valor_a, valor_b):
        return valor_a / valor_b


calculadora = calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicação(10, 5))
print(calculadora.divisão(100, 2))



