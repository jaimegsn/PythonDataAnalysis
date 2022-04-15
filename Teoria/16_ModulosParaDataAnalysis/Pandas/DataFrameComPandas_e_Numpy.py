from pandas import DataFrame
import numpy as np


data = {'Estados':['SC','CE','SP','RJ','MG','BH'], 'Ano':[2002,2003,2004,2008,2021,2012],
        'Populacao':[3,2.2,12,8.3,4.2,3.2]}

# Note que criamos uma coluna a mais
frame = DataFrame(data, columns=['Estados','Ano','Populacao','Debitos'])

frame['Debitos'] = np.arange(6.)

print(frame.describe()) # Resumo estatistico sobre o dataframe

print(frame.loc[0]) # Procura pelo indice