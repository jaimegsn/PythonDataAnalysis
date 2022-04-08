# JSON é um pacote para manipular arquivos json
import json
import os
from urllib.request import urlopen

dicionario = {'nome': 'Pedro', 'idade': 23}  # Dicionário

json.dumps(dicionario)  # Convertendo dicionario para JSON
# Também pode ser feito o inverso com dict()


# Criando um arquivo JSON:
with open('teste.json', 'w') as arquivo:
    arquivo.write(json.dumps(dicionario))

# Leitura de arquivos JSON:
with open('teste.json', 'r') as arquivo:
    data = json.loads(arquivo.read())
print(data)

# Imprimindo um arquivo JSON copiado da internet
# from urllib.request import urlopen   <- IMPORT NECESSÁRIO
response = urlopen(
    "http://vimeo.com/api/v2/video/57733101.json").read().decode('utf-8')
data = json.loads(response)[0]
print('Titulo : ', data['title'])
print('URL : ', data['url'])
print('Duração : ', data['duration'])
print('Numeros de Visualizações : ', data['stats_number_of_plays'])


# Copiando o conteudo de um arquivo para outro:
# import os   <- Necessário

arquivo_fonte = 'teste.json'
arquivo_destino = 'copia.json'

# Metodo 1:
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

# Metodo 2:
open(arquivo_destino, 'w').write((open(arquivo_fonte, 'r').read()))


# Imrpimindo copia JSON
with open(arquivo_destino, 'r') as arquivo:
    data = json.loads(arquivo.read())

print(data)
