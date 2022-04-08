# CSV é um pacote para manipular arquivos CSV
import csv

# Escrevendo arquivo
with open('teste.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(('Nome','Idade','Cidade'))
    writer.writerow(('João', '20', 'São Paulo'))

# Leitura Arquivo csv
with open('teste.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)

# Gerando uma Lista com os dados do arquivo CSV:
with open('teste.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    listaDados = list(leitor)
print(listaDados)