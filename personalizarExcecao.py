class Error(Exception): #Obrigatório criar essa classe, menos que não possua nada quando for personalizar
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        num1 = int(input('Entre com uma nota de 0 a 10: '))
        print(num1)
        if num1 > 10:
            # O comando raise força uma exceção
            raise InputError('Valor deve ser igual ou inferior a 10')
        elif num1 < 0:
            raise InputError('Nota não pode ser menor que 0')
        break # Para o while quando não houver mais erros
    except ValueError:
        print('Valor Inválido. Digite apenas números.')
    except InputError as ex:
        print(ex)