from pandas import Series
# Dict para Series em Pandas

dict1 = {'psg': 'neymar', 'bayern':'lewandowski','holanda':'roben'}
obj = Series(dict1)

# Criando uma serie e usando lista como indice:
lista = ['psg','bayern','holanda','barcelona']
obj2 = Series(dict1, index = lista)
print(obj2)

