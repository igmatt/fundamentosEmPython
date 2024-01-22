from classeTelevisao import Televisao
from classeCalculadora import Calculadora
from modulosContadorLetras import contadorletras

if __name__=='__main__':
    
    televisao = Televisao()
    print(televisao.ligada)

    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(3, 4)
    print(calculadora.soma())
    
    lista = ['ovelha', 'girafa', 'hamster']
    print('Total de letras por palavra da lista: {}'.format(contadorletras(lista)))