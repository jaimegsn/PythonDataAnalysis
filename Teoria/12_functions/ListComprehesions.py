# O list comprehension aplica uma expressão arbitraria em uma lista  ao invés de uma função
# ela é essencialmente uma linha de loop for construida dentro de []
# normalmente usamos loop for quando trabalhamos com funções map
# e usamos list comprehension quando for mais fácil de ser aplicada
# há vantagens de desempenho usar list comprehension

# Retorna cada index de uma lista:
lst = [x for x in 'python']
print(lst)  # ['p','y','t','h','o','n']


# Raiz quadrada de um range de numeros:
lst = [x**2 for x in range(0, 11)]
# Raiz quadrada de cada numero do  range
print(lst)


