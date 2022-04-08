from datetime import datetime
from datetime import date, timedelta


# Date e TimeDelta :

print(date.today())  # Imprime a data de hoje do sistema

# Criando um objeto data
dia_primeiro = date(2021, 1, 1)
print(dia_primeiro)

print(dia_primeiro.year)  # 2021   imprime apenas o ano
print(dia_primeiro.month)  # 1     imprime apenas o mes
print(dia_primeiro.day)  # 1       imprime apenas o dia

diferenca_dias = date(2021, 5, 4) - date(2021, 1, 25)
print(diferenca_dias+1)  # 100 days, 0:00:00 (Saida do tipo TIMEDELTA)
# existe um erro no calculo por isso +1

# É possivel somar uma data e uma quantidade de dias. desde que seja um objeto date com um timedelta ex:
hoje = date(2021, 5, 14)
intervalo_dias = timedelta(days=28)
dia_futuro = hoje + intervalo_dias


# DateTime :

hora_atual = datetime.now()
print(hora_atual)  # 2021-05-14 21:07:34.264714

# Para declarar uma variável desse tipo, precisamos, primeiro, passar os argumentos obrigatórios, como ano, mês e dia,
# depois podemos passar os opcionais, como hora, minuto, segundo e microssegundo.
d1 = datetime(2021, 5, 15)
d2 = datetime(2021, 5, 15, 18, 1, 59, 123456)
d3 = datetime(2021, 5, 15, 18, 1, 59)

print(d2.hour, d2.minute, d2.second, d2.microsecond)  # 18 1 59 123456


# Para saber o dia da semana utilizamos o weekday e o isoweekday
# A diferença é que os valores da primeira função vão de 0 a 6, e os da segunda função variam entre 1 e 7

dia_primeiro = datetime(2021, 1, 1)
print(dia_primeiro.weekday(), dia_primeiro.isoweekday())  # 4 5

print(
    f"01 de Janeiro de 2021 é o dia {dia_primeiro.weekday()}, logo uma sexta-feira")
# 01 de Janeiro de 2021 é o dia 4, logo uma sexta-feira

# Note a diferença de valores entre as funções e no nosso exemplo, weekday retorna 4, ou seja, considerando
# segunda-feira como dia 0, sexta-feira possui valor 4.


# Converte data em String:
data_inicio = date(2021, 1, 25)
print(data_inicio.strftime("%d/%m/%Y"))  # 25/01/2021

#Converte String em data :
data_string1 = "02 de Abril de 1900"
data1 = datetime.strptime(data_string1, "%d de %B de %Y")


# A tabela a seguir mostra os principais códigos úteis do strftime. Estes códigos serão utilizados no decorrer desta aula para
# você consolidá-los bem

# %A	Nome do dia da semana completo	    Monday, Tuesday, …, Sunday
# %d	Número do dia da semana	            01, 02, …, 31
# %b	Nome do mês de forma abreviada	    Jan, Feb, Mar, ... , Dec
# %B	Nome do mês completo	            January, February, …, December
# %m	Número do mês	                    01, 02, …, 12
# %y	Dois últimos dígitos do ano	        01, 02, …, 99
# %Y	Número do ano completo	            0001, 0002, …, 2021, ...,
# %H	Número da hora	                    01, 02, …, 24
# %M	Número do minuto	                01, 02, …, 59
# %S	Número do segundo	                01, 02, …, 59
# %j	Número do dia do ano	            001, 002, …, 365, 366
# %W	Número da semana do ano	            00, 01, …, 53

# Para gerar as datas em português, é preciso fazer uma configuração simples:
# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR')

