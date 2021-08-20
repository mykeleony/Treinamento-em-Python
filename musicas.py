import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('musicasbd.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artista;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Musica;

CREATE TABLE Artista (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artista_id  INTEGER,
    titulo   TEXT UNIQUE
);

CREATE TABLE Musica (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    titulo TEXT  UNIQUE,
    album_id  INTEGER,
    tamanho INTEGER, classificacao INTEGER, contagem INTEGER
);
''')


nomearq = input('Insira o nome do arquivo com as músicas: ') # Nesse programa, o arquivo utilizado foi o "Library.xml".

# Padrão XML:  
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def procurar(d, key):
#Função que procura as tags "key" no arquivo XML.
    
    achado = False
    for filho in d:
        if achado : return filho.text
        if filho.tag == 'key' and filho.text == key:
            achado = True
    return None

# Criando a árvore XML e extraindo todo o seu conteúdo:
coisas = ET.parse(fname)
tudo = coisas.findall('dict/dict/dict')

print('Contagem de dicionários:', len(tudo))

for entrada in tudo:
    if (procurar(entrada, 'Track ID') is None):
      continue      # Ignorando id's nulos/inexistentes.

    nome = procurar(entrada, 'Name')
    artista = procurar(entrada, 'Artist')
    album = procurar(entrada, 'Album')
    contagem = procurar(entrada, 'Play Count')
    classificacao = procurar(entrada, 'Rating')
    tamanho = procurar(entrada, 'Total Time')

    if nome is None or artista is None or album is None:  # Caso algum atributo esteja ausente, a música é ignorada.
        continue

    print(nome, artista, album, contagem, classificacao, tamanho)
    
    # Inserindo as informações no banco de dados:
    cur.execute('''INSERT OR IGNORE INTO Artista (nome) VALUES ( ? )''', ( artista,))
    cur.execute('SELECT id FROM Artista WHERE nome = ?', (artista,))
    artista_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (titulo, artista_id) VALUES (?, ?)''', ( album, artista_id ))
    cur.execute('SELECT id FROM Album WHERE titulo = ?', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Musica (titulo, album_id, tamanho, classificacao, contagem)
    VALUES ( ?, ?, ?, ?, ? )''', (nome, album_id, tamanho, classificacao, contagem))
  
    conn.commit()
