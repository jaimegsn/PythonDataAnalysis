# Diferença ERRO vs EXCEÇÕES:

# ERRO: (Erro claro de sintaxe)
# while True
#    print('teste')

# EXCEÇÕES: (Porém mesmo quando uma expressão está sintaticamente correta poderá ocorrer erros nesses casos : exceções)

# Exemplo de uma calculadora e executar a divisão por zero

#Podemos tratar exceções em Python da seguinte forma:

# try:
#    linha de codigo
# except 1:
#    se houver a exceção 1 execute esse bloco 
# except 2:
#    se houver a exceção 2 execute esse bloco
# else:
#    se não houver exceção execute esse bloco

#Temos ainda a plavra Reservada Finally, que nos permite executar o código, mesmo que exceções ocorram

# print(8+'a') #Irá Gerar um TypeError

#tratamentos:
try:
    8 +'a'
except TypeError:
    print("Operação Inválida")

def calc():
    while True:
        try:
            nmr = int(input("Digite um número"))
        except:
            print("Você não Digitou um número")
            continue
        else:
            print("Obrigado por Digitar um Número")
            break
        finally:
            print("Fim de uma iteração")





