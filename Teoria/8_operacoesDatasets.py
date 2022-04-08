# Abrindo o DataSet em uma única linha :

f = open('Teoria/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
# print(rows)
f.close()

# Dividindo um DataSet Em colunas:
f = open('Teoria/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
#print(full_data)


# Contando as linhas de um arquivo
f = open('Teoria/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data=[]
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)

count = 0
for row in full_data:
    count +=1
print(count)


# Contando o número de colunas de um arquivo 
f = open('Teoria/arquivos/salarios.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
count = 0

for colunm in first_row:
    count +=1
print(count)


# Gravando arquivo pelo Jupyter Notebook (Só funciona no JUPYTER):
# %%writefile arquivos/teste.txt
#conteudo do arquivo

