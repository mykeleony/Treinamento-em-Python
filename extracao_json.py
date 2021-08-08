'''
Extracao de dados na web em JSON:
Programa que identifica todos os numeros contidos em um codigo JSON e retorna sua soma.
Myke Leony dos Santos Amorim. 03 de maio de 2021.
'''

from urllib.request import urlopen
import json
import ssl

url = input('Insira a URL: ')
print('Acessando', url)

# Ignorando erros de certificacao SSL (https):
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

pagecode = urlopen(url, context = ctx).read()   #Conectando-se à pagina e lendo seu conteudo.
jcode = json.loads(pagecode)                    #Convertendo o codigo JSON às estruturas de dados Python.

print('A pagina contem', len(pagecode) ,'caracteres')

total = kcount = 0

for key in jcode["comments"]:
    num = int(key["count"])     # Para cada key nos dicionarios "comments", o programa extrai o valor da tag "count".

    total += num                # Adicionando o valor à soma total.
    kcount += 1                 # Contando a quantidade de numeros no codigo JSON.

print('Contagem:', kcount)
print('Soma:', total)
