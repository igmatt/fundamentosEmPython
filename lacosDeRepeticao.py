# Laços de Repetição FOR RANGE

# Descobrindo numéros primos
numero1 = int(input('Digite um número: '))
div = 0

for numeracao in range(1, numero1 + 1):
    resto = numero1 % numeracao
    print(numero1, resto)
    if resto == 0:
        div += 1
        
if div == 2:
    print('Número {} é primo!'.format(numero1))
else:
    print('Número {} não é primo!'.format(numero1))
    

for numeros in range(100):
    div = 0

    for numeracao in range(1, numeros + 1):
        resto = numeros % numeracao
        if resto == 0:
            div += 1
            
    if div == 2:
        print('Número {} é primo!'.format(numeros))


# Laço de repetição WHILE

numero2 = 0

while numero2 <= 10:
    print(numero2)
    numero2 += 1
    
nota1 = int(input('Digite a nota: '))
while nota1 > 10:
    nota1 = int(input('Nota 1  incorreta. Digite uma nota: '))
    
nota2 = int(input('Digite a nota: '))
while nota2 > 10:
    nota2 = int(input('Nota 2  incorreta. Digite uma nota: '))
    
nota3 = int(input('Digite a nota: '))
while nota3 > 10:
    nota3 = int(input('Nota 3  incorreta. Digite uma nota: '))
    
nota4 = int(input('Digite a nota: '))
while nota4 > 10:
    nota4 = int(input('Nota 4  incorreta. Digite uma nota: '))

mediaNota = (nota1 + nota2 + nota3 + nota4) / 4

print('A média é : {}'.format(mediaNota))
