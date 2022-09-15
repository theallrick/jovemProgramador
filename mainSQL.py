import sqlite3
class Netflix():
    conexao = sqlite3.connect('perfil.db')
    cursor = conexao.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS perfil('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'senha TEXT'
    ')')