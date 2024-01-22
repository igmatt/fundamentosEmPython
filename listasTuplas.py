# LISTA

listaNumeros = [19, 13, 5, 7]
listaAnimais = ['gato', 'cachorro', 'girafa', 'hamster']

soma = 0

for lista in listaNumeros:
    print(lista)
    soma += lista
print(soma)

# Outro método
print (sum(listaNumeros))

# Maior e menor valor da lista
print(max(listaNumeros))
print(min(listaNumeros))

print(max(listaAnimais))
print(min(listaAnimais))

if 'lobo' in listaAnimais:
    print ('Existe o animal na lista')
else:
    print ('Não existe o animal na lista')
    listaAnimais.append('lobo')
    print(listaAnimais)


#Adicionando item na lista
if 'lobo' in listaAnimais:
    print ('Existe o animal na lista')
else:
    print ('Não existe o animal na lista, será incluído')
    listaAnimais.append('lobo')
    print('Nova Lista de Animais: ', listaAnimais)
    
#Retirando item da lista ( POP retira o último item se não especificar)
listaAnimais.pop(2)
print('Nova Lista de Animais: ', listaAnimais)

#Retirando item da lista especificando pelo nome
listaAnimais.remove('girafa')
print('Nova Lista de Animais: ', listaAnimais)

#Ordenar a lista
listaNumeros.sort()
listaAnimais.sort()

print(listaNumeros)
print(listaAnimais)

#Reverter a lista
listaNumeros.reverse()
listaAnimais.reverse()

print(listaNumeros)
print(listaAnimais)

# Substitui item na lista referente a posição
listaNumeros[3] = 15
print (listaNumeros)


# TUPLAS ( são imutaveis )
tuplaNumeros = ( 1, 10, 12, 18)
print(tuplaNumeros[0])

#Contador
print(len(listaNumeros))
print(len(listaAnimais))

# Converter Listas em Tuplas

tuplaAnimais = tuple(listaAnimais)
print(type(tuplaAnimais))
print(tuplaAnimais)

# Convertendo Tupla em lista
listaNumeros = list(tuplaNumeros)
print(type(listaNumeros))
print(listaNumeros)