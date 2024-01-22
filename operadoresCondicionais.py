#Estrutura condicional e Operadores Lógicos

numero1 = int(input('Número 01: '))
numero2 = int(input('Número 02: '))
numero3 = int(input('Número 03: '))

if numero1>numero2 and numero1 > numero3:
    print('O maior número é {}'.format(numero1))
    
elif numero2 > numero1 and numero2 > numero3:
    print('O maior número é {}'.format(numero2))
    
else :
    print('O maior número é {}'.format(numero3))
    

numero4 = int(input('Digite um número: '))
numero5 = int(input('Digite um número: '))

restoNumero4 = numero4%2
restoNumero5 = numero5%2

if restoNumero4 == 0 or restoNumero5 == 0:
    print('Foi digitado um número par!')
else:
    print('Nenhum número digitado é par!')
    
    
    
nota1 = int(input('Digite a nota: '))
if nota1 > 10:
    nota1 = int(input('Digite uma nota superior ou igual a 10: '))
    
nota2 = int(input('Digite a nota: '))
if nota2 > 10:
    nota2 = int(input('Digite uma nota superior ou igual a 10: '))
    
nota3 = int(input('Digite a nota: '))
if nota3 > 10:
    nota3 = int(input('Digite uma nota superior ou igual a 10: '))
    
nota4 = int(input('Digite a nota: '))
if nota4 > 10:
    nota4 = int(input('Digite uma nota superior ou igual a 10: '))

mediaNota = (nota1 + nota2 + nota3 + nota4) / 4

print('A média é : {}'.format(mediaNota))
