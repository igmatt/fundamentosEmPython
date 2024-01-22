lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]
    variavel1 = variavel2
    #Não chega a fechar o arquivo, porque já tem um erro!
    #print('Fechando arquivo')
    #arquivo.close()
#except ZeroDivisionError:
#    print('Não é possível dividir por 0!')
except ArithmeticError: #Não posso colocar erro de divisão, já que envolve outros erros esse tratamento
    print('Houve um erro de operação aritimética!')
except IndexError:
    print('Não existe o índice desejado!')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else: #quando não tem erro, ele executa essa mensagem
    print('Executar quando não houver Exceção')
finally: # Com erro ou não, sempre vai executar
    print('Sempre Executa')
    print('Fechando arquivo')
    arquivo.close()