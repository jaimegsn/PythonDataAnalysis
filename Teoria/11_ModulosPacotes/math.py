import math

print(math.pi)  # pi 3,14.....

print(math.inf)  # inf      constante ‘infinito’, com valor positivo
print(-math.inf)  # -inf    constante ‘infinito’, com valor negativo

# True       comparação do infinito com o valor cem bilhões, provando que infinito é maior
print(math.inf > 100000000000)

# False     utilizando o método isinf para saber se o elemento é infinito.
print(math.isinf(100000000000))

# True          utilizado o método isinf para saber se o elemento é infinito.
print(math.isinf(math.inf))

print(math.nan)  # nan ->é chamada a constante NaN (Not a Number), que indica que uma variável que deveria ser numérica foi corrompida

# False    foi utilizado o método isnan para saber se o elemento é um NaN
print(math.isnan(10))

# TypeError    foi utilizado o método isnan para saber se o elemento é um NaN
print(math.isnan('Texto'))

# True    foi utilizado o método isnan para saber se o elemento é um NaN
print(math.isnan(math.nan))


print(math.ceil(9.24))  # 10    arredonda para cima
print(math.ceil(-9.24))  # -9   arredonda para cima

print(math.floor(9.89))  # 9   arredonda para baixo
print(math.floor(-9.89))  # -10  arredonda para baixo

print(math.trunc(9.80))  # 9    eliminar a parte decimal e manter a inteira
print(math.trunc(-9.80))  # -9  eliminar a parte decimal e manter a inteira

print(math.fabs(2.3))  # 2.3   retorna o valor absoluto
print(math.fabs(-2.3))  # 2.3  retorna o valor absoluto


print(math.pow(10, 2))  # 100.0   retorna o valor elevado ao expoente

print(math.sqrt(100))  # 10.0   retorna a raiz quadrada

print(math.log(100, 10))  # 2.0  retorna o logaritmo de base 10

print(math.factorial(5))  # 120   retorna o fatorial de um número


print(math.isclose(10, 8, rel_tol=0.2))  # True
# isclose determina se dois números estão próximos é possível definir a tolerância de
# proximidade. Foi empregado o parâmetro rel_tol para a tolerância, que é um valor em porcentagem.
# Nesse caso, é 20%, e para saber se o número está próximo usamos essa fórmula: x-(x*0.2) <= y <= x+(x*0.2),
# em que x é o maior valor e y é o menor valor passado como argumento.

print(math.isclose(10, 5, abs_tol=5))  # True
# foi usado o parâmetro abs_tol para a tolerância, que é um valor absoluto. Nesse caso, é 5, ou seja, para saber se o
# número está próximo, é usada a fórmula: |x-y| <= 5, onde x e y são os valores passados como argumento.

print(math.gcd(10, 15))  # 5
# o método gcd (MDC, Maior Divisor Comum), que calcula o maior número inteiro que divide os dois números.


# 5.0  Calcula a hipotenusa de um triângulo retângulo, de acordo os outros 2 lados do triângulo.
math.hypot(3, 4)

# 2.23606797749979   Calcula a distância entre dois pontos no plano cartesiano.
print(math.dist((1, 3), (3, 2)))
