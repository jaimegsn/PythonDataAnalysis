# A função reduce aplica a função passada como parametro a todos os elementos até que reste apenas um elemento
from functools import reduce
lista = [1, 2, 3, 4, 5]

somaElementosLista = reduce(lambda x,y:x+y , lista) # 1+2+3+4+5 = 15
print(somaElementosLista)

#reduce(funcao,sequencia)