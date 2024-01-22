def contadorletras(listaPalavras):
    contador = []
    
    for palavras in listaPalavras:
        quantidade = len(palavras)
        contador.append(quantidade)
    return contador

if __name__=='__main__':
    
    lista = ['cachorro', 'gato']
    print(contadorletras(lista))