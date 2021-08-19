'''
Programa que utiliza banco de dados para estabelecer um ranqueamento dos domínios de e-mail que mais enviam correios eletrônicos em uma lista de e-mails.
Myke Leony dos Santos Amorim. 05 de maio de 2021.
'''

import sqlite3
import re

conn = sqlite3.connect('dominios_email.sqlite')
cur = conn.cursor()                                 # Objeto que permite a execucao de comandos SQL.

cur.execute('DROP TABLE IF EXISTS Contagem')        #Verificando se ha uma tabela "Contagem" preexistente. Se existir, esta sera excluida.
cur.execute('''
CREATE TABLE Contagem (
    dominio    TEXT,
    total      INTEGER
)
''')                                                # Criando a tabela "contagem".

nomearq = input('Insira o nome do arquivo contendo os e-mails: ') # Nesse exercício, o arquivo usado é o "mbox.txt".
arq = open(nomearq)

for linha in arq:
    if not linha.startswith('From: '):
        continue

    partes = linha.split()                          # Fatorando a linha contendo o email em partes.
    email = partes[1]                               # O segundo elemento da lista de pedacos eh o correspondente ao email.

    ''' Encontrando e extraindo o dominio do email com expressoes regulares:
    O programa busca pela parte da string que contem '@' e extrai os caracteres pospostos.
    Em seguida, como o retorno eh uma lista, retira-se seu primeiro elemento e, portanto, converte-o a string. '''

    dominio = (re.findall('@(.+)', email))[0]

    ''' Para cada email encontrado, faz-se um select no banco de dados para verificar se o campo "total" esta vazio.
    Se sim, insere-se o valor 1 a esse campo. Caso contrario, o valor anterior eh acrescido em 1. '''

    cur.execute('SELECT total FROM Contagem WHERE dominio = ?', (dominio,))     # Os parenteses e a virgula sao necessarios para transformar o elemento em uma tupla.
    campo = cur.fetchone()

    if campo is None:
        cur.execute('INSERT INTO Contagem (dominio, total) VALUES (?, 1)', (dominio,))

    else:
        cur.execute('UPDATE Contagem SET total = total+1 WHERE dominio = ?', (dominio,))

conn.commit()   # Gravando as alteracoes no banco.

ranking = 'SELECT * FROM Contagem ORDER BY total DESC LIMIT 10'                 # Exibindo um "top 10" dos maiores enviadores de e-mails.

for campo in cur.execute(ranking):
    print(str(campo[0]), campo[1])

cur.close()
