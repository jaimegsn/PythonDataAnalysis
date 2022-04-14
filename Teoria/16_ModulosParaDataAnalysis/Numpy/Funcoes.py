# Outra forma de criar um Array:
import numpy as np

# A função arange cria um vetor contendo uma progressão aritmética a partir de um intervalo - Start, Stop, Step
vetor2 = np.arrange(0., 4.5, .5) 


# Cria um vetor com 10 elementos todo preenchido com zeros ([0,0,0...])
vetor3 = np.zeros(10)


# Cria um vetor com 1 nas posições diagonais e 0 no restante
vetor4 = np.eye(3) # (qtd dimensao)

# Os valores passados como parâmetro, formam uma diagonal o resto é zero:
vetor5 = np.diag(np.array([1,2,3,4]))

# Array de valores booleanos 
vetor6 = np.array([True,False,False,True])

