
# Métodos para tratar arquivos :

# open() Usada para abrir o arquivo
# read() Leitura do arquivo
# write() Gravação no arquivo
# seek() Retorna para o início do arquivo
# readlines() Retorna a lista de linhas do arquivo
# close() Fecha o arquivo


# Leitura e Gravação de Arquivo:
# OBS o path do seu arquivo depende de onde você está no TERMINAL(Vs Code)


# Abrindo o arquivo para leitura(r):
arq1 = open('Teoria/arquivos/arquivo1.txt', 'r')

print(arq1.read())  # Lendo o arquivo
print(arq1.tell())  # Contar o numero de caracteres
# print(arq1.seek(2,0))  Pesquisar SOBRE
print(arq1.read(5))  # Lendo o arquivo com um numero especifico de caracteres(5)
arq1.close()  # Fechar o Arquivo

# Abrindo o arquivo para escrita(w):
arq2 = open('Teoria/arquivos/arquivo1.txt', 'w')
arq2.write("Escrevendo no arquivo")

arq2.close()  # Fechar o Arquivo


# Abrindo o arquivo para Acrescentar no conteudo(a):
arq3 = open('Teoria/arquivos/arquivo1.txt', 'a')
arq3.write("Acrescentando ao conteudo")

arq3.close()  # Fechar o Arquivo
