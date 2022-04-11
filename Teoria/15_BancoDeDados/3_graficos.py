# Principal biblioteca pra a criação de Gráficos : matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import sqlite3
import datetime
import os

os.remove('bdGraphic.db') if os.path.exists('bdGraphic.db') else None

conn= sqlite3.connect('bdGraphic.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS vendas (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
    'date TEXT, modelo varchar(140), valor REAL, nome TEXT)')


# Dados ficticios:
data = [
    ("17/03/2018","Fiat","67175.0","Bravo T-Jet"),
    ("31/02/2018","Fiat","90175.0","Strongest"),
    ("07/09/2018","Honda","120175.0","Veloster"),
    ("01/08/2018","Honda","30175.0","Richester"),
    ("23/06/2018","Audi","90175.0","Hotwheels")
    ]  

for d in data:
    c.execute('INSERT INTO vendas (date,modelo,valor,nome) VALUES (?,?,?,?)',d)


# Criar o gráfico:

def dados_graficos():
    c.execute('SELECT modelo,valor FROM vendas')
    marcas=[]
    valores=[]
    dados = c.fetchall()
    for linha in dados:
        marcas.append(linha[0])
        valores.append(linha[1])
    
    plt.bar(marcas,valores)
    plt.show()

dados_graficos()


