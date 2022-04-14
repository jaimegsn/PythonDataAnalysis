# Um array NumPy é um conjunto de valores, todos do mesmo tipo e indexados por uma tupla de valores
# não negativos      Porque usar ? :

# Arrays NumPy são homogeneos e possuem tipos estáticos
# Arrays NumPy são mais eficientes no uso de memória
# Arrays NumPy oferecem rápidas implementações de funções matemáticas
# Arrays NumPy são uma opção mais rápida e mais poderosa que listas

# Criando arrays :
import numpy as np 
print(np.__version__) # Saber a versão do pacote

# Array unidimensional criado a partir de uma lista:
vetor1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]) 

# Verificar a dimensal do array: 
print(vetor1.shape) # (9,)



