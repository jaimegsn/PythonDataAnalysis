from pandas import DataFrame

data = {'Estados':['SC','CE','SP','RJ','MG','BH'], 'Ano':[2002,2003,2004,2008,2021,2012],
        'Populacao':[3,2.2,12,8.3,4.2,3.2]}

frame = DataFrame(data)
frameMudandoIndex = DataFrame(data,index = ['um','dois','tres','quatro','cinco','seis'])


# Imprimir indices:
print(frame.index)

# Imprimir valores:
print(frame.values)

# Imprimir colunas:
print(frame.columns)

