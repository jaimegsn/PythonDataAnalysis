# enquanto-faça (WHILE)
# while condição :
a = 5
while a < 10:
    print(a)
    a += 1


# para-cada-em (FOR IN)
# for item in lista:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista:
    print(numero)


#para-de-até (FOR)
# for x in range(5) :
for x in range(5):
    print(x)

# ______________________________________________________________________________
# IMPORTANTE :  PASS,BREAK,CONTINUE
# Continue -> Pula uma iteração para a próxima iteração
# Break -> Finaliza o laço de repetição
# Pass -> Não faz nada

teste = 5
while teste > 0:
    teste -= 1
    if teste == 3:  # Se teste for igual a 3 pule para a prox iteração = 2
        continue
    print(teste)
    if teste == 2:  # Se teste for igual a 2 quebre o laço
        break
