contadorLetras = lambda lista: [len(nomes) for nomes in lista ]

listaAnimais = ['gato', 'doninha', 'cavalo']
print(contadorLetras(listaAnimais))

soma = lambda num1, num2: num1 + num2
subtracao = lambda num1, num2: num1 - num2

print(soma(1, 3))
print(subtracao(2, 0))

calculadora = {
    'soma': lambda num1, num2: num1 + num2,
    'subtração:': lambda num1, num2: num1 - num2,
    'multiplicacao': lambda num1, num2: num1 * num2,
    'divisão': lambda num1, num2: num1 / num2
}

soma = calculadora['soma']
multiplicacao = calculadora ['multiplicacao']
print('Soma: {}'.format(soma(17, 3)))
print('Multiplicação: {}'.format(multiplicacao(5, 2)))