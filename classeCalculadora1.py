#Outra forma informando valores distintos direto no print

class Calculadora1: # Classe
    
    def __init__(self):
        pass # Apenas para não deixar o init vazio 
        
    def soma(self, valor1, valor2): #Funções
        return valor1 + valor2

    def subtracao(self, valor1, valor2):
        return valor1 - valor2
            
    def multiplicacao(self, valor1, valor2):
        return valor1 * valor2

    def divisao(self, valor1, valor2):
        return valor1 / valor2

if __name__=='__main__':

    calculadora = Calculadora1()

    print('Soma: {}'.format(calculadora.soma(10, 2)))
    print('Subtração: {}'.format(calculadora.subtracao(5, 3)))
    print('Multiplicação: {}'.format(calculadora.divisao(5, 4)))
    print('Divisão: {}'.format(calculadora.divisao(20, 4)))