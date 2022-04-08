import random
print(random.random())  # Gera numero aleatorio 0.4288890546751146...


# Gera numeros aleatorios entre 10 e 20 -> 16.014634495610515 :
print(random.uniform(10, 20))

# Gera numeros inteiros aleatorios entre 1 e 6 -> 1...6 :
print(random.randint(1, 6))

# Gera um elemento aleatorio de uma lista :
dado = [1, 2, 3, 4, 5, 6]
print(random.choice(dado))  # 5


# Com CHOICES podemos definir pesos de sorteio na lista:
dado = [1, 2, 3, 4, 5, 6]
pesos = [1, 1, 1, 1, 2, 4]  # 10% 10% 10% 10% 20% 40%
print(random.choices(dado, weights=pesos))  # [6]


# Sample vs Choices = Sample não repete o valor sendo utilizado mais para amostras enquanto o Choices
# pode repetir o valor da lista:
baralho = ['Ás de Copas', '2 de Copas', '3 de Copas', '4 de Copas', '5 de Copas', '6 de Copas', '7 de Copas',
           '8 de Copas', '9 de Copas', '10 de Copas', 'Valete de Copas', 'Dama de Copas', 'Rei de Copas']

print(random.choices(baralho, k=2))  # ['Valete de Copas', 'Valete de Copas']

print(random.sample(baralho, k=2))  # ['10 de Copas', '3 de Copas']


# Embaralhar uma lista de forma aleatória :
baralho = ['Ás de Copas', '2 de Copas', '3 de Copas', '4 de Copas', '5 de Copas', '6 de Copas', '7 de Copas',
           '8 de Copas', '9 de Copas', '10 de Copas', 'Valete de Copas', 'Dama de Copas', 'Rei de Copas']
random.shuffle(baralho)
