import sqlite3

conexao = sqlite3.connect('netflix.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS contas('
'id INTEGER PRIMARY KEY AUTOINCREMENT,'
'email TEXT,'
'senha TEXT'
')')

#cursor.execute('INSERT INTO clientes(nome,peso) VALUES("antonio",80)')
#cursor.execute('INSERT INTO clientes(nome,peso) VALUES(?,?)',('Aline',60))
#conexao.commit()
#cursor.execute('UPDATE clientes SET peso = ? WHERE id =2',(58,))
#conexao.commit()
#cursor.execute('DELETE FROM clientes WHERE id =2')
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    print(linha)

cursor.close() 
conexao.close()