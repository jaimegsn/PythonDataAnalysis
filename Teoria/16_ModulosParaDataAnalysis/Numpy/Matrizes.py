import numpy as np

# Criando uma matriz Bidimensional:
matriz = np.array([[1,2,3],[4,5,6]])
print(matriz)
print(matriz.shape)

# Criando uma matriz 2x3 apenas com numeros '1' :
matriz1 = np.ones((2,3))

# Criando uma matriz a partir de uma lista de listas:
lista =[[2,3,4],[1,9,8],[12,33,24]]
matriz2 = np.matrix(lista)

print(matriz2[2,1]) # Imprimir linha 2 coluna 1

x = np.array([1,2]) # NumPy decide o tipo dos dados
y = np.array([1.0,2.0]) # NumPy decide o tipo dos dados
z = np.array([5,7], dtype=np.float64) # Forçamos um tipo de dado em particular

