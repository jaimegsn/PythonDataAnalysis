# A função filter oferece uma maneira conveniente para filtrar todos os elementos de uma sequência, para os quais
# a função retorne true, ou seja cria uma nova lista de elementos da lista que obedecem aos requisitos da função
# retornando true:

lista = [1, 2, 3, 4, 5]
filtro = list(filter(lambda x:x%2==0 , lista))
print(filtro)

#filter(funcao,sequencia)