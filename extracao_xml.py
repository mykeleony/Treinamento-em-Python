'''
Programa que lê um arquivo XML em uma página web, extrai todos os números e os soma.
Myke Leony dos Santos Amorim. 04 de maio de 2021.
'''

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

url = input('Insira o link contendo o arquivo XML: ')
print('Acessando', url)

# Ignorando erros de certificação SSL (HTTPS):
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cod = urlopen(url, context = ctx).read().decode()       # Convertendo os bytes XML a caracteres em strings.

print('Acessados', len(cod), 'caracteres')

arvore = ET.fromstring(cod)                            # Criando a árvore de elementos XML.
felementos = tree.findall('comments/comment')            # Extraindo todas as tags "comment" contidas no elemento pai.

total = 0

for count in felementos:
    total += int(count.find('count').text)              # Para todos os elementos "comment", o programa busca o elemento "count", extrai seu conteúdo (um número inteiro) e o adiciona à soma.
    

print('Counts:', len(felementos))                         # Informing how much "count" elements exists in the XML code.
print('Soma:', total)
