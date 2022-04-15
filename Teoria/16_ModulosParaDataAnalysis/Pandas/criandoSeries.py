from pandas import Series
import pandas as pd

# Criando uma serie sem especificar os índices (ele cria automaticamente)
obj = Series([67, 78, 32, 12])

print(obj.values)  # Mostra os valores


# Onde o indice starta termina(exclusivo) e os saltos  (start,stop,step):
print(obj.index)

# Busca todos os valores de OBJ que são maiores que 70:
print(obj[obj>70]) 
