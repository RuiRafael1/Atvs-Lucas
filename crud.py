#baixar o drive do mysql com a seguinte linha de código
#pip install mysql-connector-python

import mysql.connector

conexao = mysql.connector.connect(
host = '127.0.0.1/3308',
user = 'root',
password = None,
database = 'teste',
)

cursor = conexao.cursor()
#comando = ''
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados
#resultado = cursor.fetchall() # ler o banco de dados

#CREAT
produto = "teclado"
valor = 100
comando = f'INSERT INTO vendas (produto, valor) VALUES ("{produto}", {valor})'
cursor.execute(comando)
conexao.commit()
cursor.close()
conexao.close()

#READ
# comando = 'SELECT * FROM b_pmt.vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# print(resultado)
# cursor.close()
# conexao.close()

#UPDATE
# nome_produto = "mouse"
# valor = 50
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()
# cursor.close()
# conexao.close()

#DELETE
# nome_produto = "mouse"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()
# cursor.close()
# conexao.close()