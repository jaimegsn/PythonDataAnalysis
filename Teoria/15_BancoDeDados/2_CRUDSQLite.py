import sqlite3
import os
os.remove('prod.db') if os.path.exists('prod.db') else None

conexao = sqlite3.connect('prod.db')
cursor = conexao.cursor()


def createTable(query):
    cursor.execute(query)
    conexao.commit()

def inserirDados(query,values):
    cursor.execute(query,values)
    conexao.commit()

def mostrarDados(query):
    cursor.execute(query)
    for linha in cursor.fetchall():
        print(linha)


def atualizarDados(query):
    cursor.execute(query)
    conexao.commit()

def removerDados(query):
    cursor.execute(query)
    conexao.commit()
    

#Query para criar o a tabela com os atributos:
create = 'CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
    'date TEXT, categoria varchar(140), valor REAL, nome TEXT)'

insert = 'INSERT INTO produtos (date,categoria,valor,nome) VALUES (?,?,?,?)'

select = 'SELECT * FROM produtos'
select2 = 'SELECT * FROM produtos WHERE valor > 1000.0'

update = 'UPDATE produtos SET valor = 2500.0 WHERE valor = 2000.0'

delete = 'DELETE FROM produtos WHERE valor = 2500.0'





createTable(create)
inserirDados(insert,("2022/03/12","Informática","2000","celular"))
mostrarDados(select)
atualizarDados(update)
mostrarDados(select)
removerDados(delete)
mostrarDados(select)





