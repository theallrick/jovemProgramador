#Crie um algoritmo onde um banco possa criar uma tabela de clientes e adiciona-los
#Cliente deve ter ID, Nome, Saldo, Numero de Conta e Agencia.
#O algoritmo deve ser capaz de adicionar uma pessoa diferente a cada execução.
#E deve imprimir uma lista com todos os clientes, mostrando nome, numero de conta  e saldo.
import sqlite3

conexao = sqlite3.connect('ContasDoBanco.db')
cursor = conexao.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS contas('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'nome TEXT,'
'saldo INTEGER,'
'numeroDeConta TEXT,'
'agencia TEXT'
')')
cursor.execute('INSERT INTO contas(nome,saldo,numeroDeConta,agencia) VALUES("Henrique",2420,123,"bradesco")')
cursor.execute('INSERT INTO contas(nome,saldo,numeroDeConta,agencia) VALUES("Willian",1000,420,"Itau"),("Aline",420,764,"Caixa")')
conexao.commit()
cursor.execute('UPDATE contas SET saldo = ? WHERE id =2',(500,))
conexao.commit()

cursor.execute('SELECT * FROM contas')
for linha in cursor.fetchall():
    print(linha)

cursor.close() 
conexao.close()