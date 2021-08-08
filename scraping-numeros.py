'''
Web scraping simples utilizando BS4 e SSL.
Myke Leony dos Santos Amorim. 02 de maio de 2021.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup       #Biblioteca útil à limpeza de codigo.
import ssl

#Ignorando erros de certificacao SSL (https).
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
nastyhtml = urlopen(url, context = ctx).read()   #Inserindo o codigo HTML em uma string.
html = BeautifulSoup(nastyhtml, "html.parser")   #"Limpando" o codigo.

spans = html('span')                             #Os numeros estao contidos nas tags "span" da pagina.

sum = 0

for span in spans:
    sum = sum+int(span.contents[0])         #span.contents[0] retorna o texto (numero) da tag.

print(sum)
