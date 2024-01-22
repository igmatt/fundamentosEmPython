# Funções Tudo que retorna valor /  Métodos  Não retorna valor

class Calculadora: # Classe
    
    def __init__(self, numero1, numero2):
        self.valor1 = numero1
        self.valor2 = numero2
        
    def soma(self): #Funções
        return self.valor1 + self.valor2

    def subtracao(self):
        return self.valor1 - self.valor2
            
    def multiplicacao(self):
        return self.valor1 * self.valor2

    def divisao(self):
        return self.valor1 / self.valor2

if __name__=='__main__':
    calculadora = Calculadora(10, 2)

    print('Soma: {}'.format(calculadora.soma))
    print('Subtração: {}'.format(calculadora.subtracao))
    print('Multiplicação: {}'.format(calculadora.divisao))
    print('Divisão: {}'.format(calculadora.divisao))
