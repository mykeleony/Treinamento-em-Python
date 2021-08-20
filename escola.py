'''
Programa que, dado um arquivo JSON contendo inúmeras informações de uma escola, organiza essas informações em um banco de dados.
Myke Leony dos Santos Amorim. 10 de maio de 2021.
'''

import json
import sqlite3

# Criando/conectando-se a o banco de dados "escola":
conn = sqlite3.connect('escola.sqlite')
cur = conn.cursor()

# Criando as tabelas do banco:
cur.executescript('''
DROP TABLE IF EXISTS Usuario;
DROP TABLE IF EXISTS Membro;
DROP TABLE IF EXISTS Curso;

CREATE TABLE Usuario (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome   TEXT UNIQUE
);

CREATE TABLE Curso (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    titulo  TEXT UNIQUE
);

CREATE TABLE Membro (
    usuario_id     INTEGER,
    curso_id   INTEGER,
    funcao        INTEGER,
    PRIMARY KEY (usuario_id, curso_id)
)
''')

# Acessando o arquivo JSON e seu conteúdo com as informações da escola.
narq = input('Insira o nome do arquivo JSON contendo as informações da escola: ')  # Nesse programa, o arquivo utilizado foi o "roster_data.json".
texto = open(narq).read()
jsoncod = json.loads(texto)

print(jsoncod[0])

for tag in jsoncod:
    # Extraindo o conteúdo das tags:
    nome = tag[0]
    titulo = tag[1]
    funcao = int(tag[2])

    print(nome, titulo)
    
    # Inserindo as informações no banco de dados:
    cur.execute('INSERT OR IGNORE INTO Usuario (nome) VALUES (?)', (nome,))
    cur.execute('SELECT id FROM Usuario WHERE nome = ?', (nome,))
    id_usuario = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Curso (titulo) VALUES (?)', (titulo,))
    cur.execute('SELECT id FROM Curso WHERE titulo = ?', (titulo,))
    id_curso = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Membro (usuario_id, curso_id, funcao)
    VALUES (?, ?, ?)''', (id_usuario, id_curso, funcao))

conn.commit()
