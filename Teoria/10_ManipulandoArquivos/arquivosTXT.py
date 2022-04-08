# OS é um pacote para manipular o sistema operaciona: manipulando arquivos,diretorios...
import os

texto = "Cientista de Dados"
texto = texto + " é uma profissão "
print(texto)

# Criando arquivo:
arquivo = open(os.path.join("teste.txt"), 'w')

# Gravando os dados no arquivo:
arquivo.write(texto)

# Fechando arquivo:
arquivo.close()

# Lendo o arquivo:
arquivo = open('teste.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)


# Podemos usar a expressão para executar um bloco de comandos que irão manipular o arquivo:

with open('teste.txt', 'r') as arquivo:  # Ele fecha o arquivo automaticamente
    conteudo = arquivo.read()
print(conteudo)


with open('teste.txt', 'w') as arquivo:  # Ele fecha o arquivo automaticamente
    arquivo.write("Sobrescrevendo")


with open('teste.txt', 'r') as arquivo:  # Ele fecha o arquivo automaticamente
    conteudo = arquivo.read()
print(conteudo)
