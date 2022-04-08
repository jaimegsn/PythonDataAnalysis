listaVazia = []

listaExemplo = [1, 2, 3, 4, 5]

print(listaExemplo)  # Imprime lista inteira
print(listaExemplo[0])  # Imprime 1° elemento da lista

listaExemplo[0] = 10  # Atualizando um item da lista
del listaExemplo[0]  # Deletando um item da lista


# Listas Aninhadas (Matrizes)
listaMatriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listaMatriz[0])  # [1, 2, 3]
print(listaMatriz[0][0])  # 1

# Concatenar Listas:
listaConc1 = [1, 2, 3, 4, 5]
listaConc2 = [6, 7, 8, 9, 10]
listaResult = listaConc1 + listaConc2
print(listaResult)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Operador in (Verifica se o elemento existe na lista)
listaTeste = [1, 2, 3, 4, 'leite']
print(1 in listaTeste)  # True
print('leite' in listaTeste)  # True
print('arroz' in listaTeste)  # False

# Funções Built-in
listaBuild = [1, 2, 3, 4, 10]
print(len(listaBuild))  # Retorna o comprimento da lista -> 5
print(max(listaBuild))  # Retorna o maior elemento da lista -> 10
print(min(listaBuild))  # Retorna o menor elemento da lista -> 1
print(sum(listaBuild))  # Retorna a soma dos elementos da lista -> 20
listaBuild.append(1)  # Adiciona um elemento na lista -> [1, 2, 3, 4, 10, 1]

# Retorna quantas vezes o elemento '1' existe na lista -> 2
listaBuild.count(1)

listaBuild.sort()  # Ordena a lista em ordem crescente -> [1, 1, 2, 3, 4, 10]
listaBuild.index(4)  # Retorna o índice do elemento '4' -> 3

# Insere o elemento 'leite' na posição 2 -> [1, 1, 'leite', 2, 3, 4, 10]
listaBuild.insert(2, 'leite')

# ..... Várias outras, pesquisar na Documentação do Python
