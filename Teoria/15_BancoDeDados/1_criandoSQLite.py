import os
import sqlite3

# Remove o arquivo do banco de dados SQLite caso ele exista :
os.remove('escola.db') if os.path.exists('escola.db') else None

# Irá conectar com o arquivo do banco de dados SQLITE 'escola.db' e caso ele não exista, ele será criado:
con = sqlite3.connect('escola.db')

# Criando um cursor:
# (Um cursor permite percorrer todos os registros em um conjunto de dados)
cur = con.cursor()

# Criando uma instrução SQL:
sql_create = 'CREATE TABLE IF NOT EXISTS cursos'\
    '(id INTEGER PRIMARY KEY,'\
    'titulo varchar(100),'\
    'categoria varchar(140))'

# Executando a instrução SQL no cursor:
cur.execute(sql_create)

sql_insert = 'insert into cursos values (?,?,?)'

# Dados que queremos inserir:
recset = [(1000, 'Ciencia de Dados', 'Data Sciente'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]

# Inserindo os registros:
for rec in recset:
    cur.execute(sql_insert, rec)

# Grava a Transação(Grava os dados no BD):
con.commit()


# Query SQL para consultar os registros:
sql_select = 'select * from cursos'

cur.execute(sql_select)  # Executa a query

# Usamos o fetchall para pegar todos os registros e salvar em dados:
dados = cur.fetchall()

for linha in dados:
    print(linha)

con.close() # Fecha a conexão
