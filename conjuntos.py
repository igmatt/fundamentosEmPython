# Conjuntos

conjuntoNumeros1 = {1, 2, 3, 4, 5}
conjuntoNumeros2 = {5, 6, 7, 8}

conjuntoNumeros1.add(6) #adicionar item
conjuntoNumeros1.discard(2) #remover item
print(conjuntoNumeros1)

conjuntoUniao = conjuntoNumeros1.union(conjuntoNumeros2)
print ('Uniao: {}'.format(conjuntoUniao))

conjuntoInterseccao = conjuntoNumeros1.intersection(conjuntoNumeros2)
print('Intersecção: {}'.format(conjuntoInterseccao))

conjuntoDiferenca1 = conjuntoNumeros1.difference(conjuntoNumeros2)
print ('Diferença Números 01: {}'.format(conjuntoDiferenca1))

conjuntoDiferenca2 = conjuntoNumeros2.difference(conjuntoNumeros1)
print ('Diferença Números 02: {}'.format(conjuntoDiferenca2))

conjuntoDifSimetrico = conjuntoDiferenca1.symmetric_difference(conjuntoDiferenca2)
print('Diferença Simétrica: {}'.format(conjuntoDifSimetrico))

conjuntoNumeros3 = {1, 2, 3}
conjuntoNumeros4 = {1, 2, 3, 4, 5}

conjuntoSubSet = conjuntoNumeros3.issubset(conjuntoNumeros4)
print ('Conjunto 3 é subconjunto do Conjunto 4? {}'.format(conjuntoSubSet)) #Verifica se um é subconjunto do outro

conjuntoSuperSet = conjuntoNumeros4.issuperset(conjuntoNumeros3)
print('Conjunto 4 é superconjunto do Conjunto 3? {}'.format(conjuntoSuperSet))

lista = ['cachorro', 'cachorro', 'gato', 'girafa']
print(lista)

conjuntoAnimais = set(lista) #Transforma em conjunto e elimina duplicidade
print(conjuntoAnimais)

listaAnimais = list(conjuntoAnimais) #Retorna para formato de LISTA
print(listaAnimais)