'''
Web scraping com BS4 e expressoes regulares:
Programa que, a partir de uma URL inicial, acessa o enesimo link contido na pagina dessa URL, repetindo o processo pela quantidade determinada pelo usuario.
Myke Leony dos Santos Amorim. 03 de maio de 2021.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

#Ignorando erros de certificacao SSL (https):
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))                 # Determinando o numero de repeticoes do acesso.

pst = int(input('Enter position: '))                # Definindo a pagina inicial do processo.

while count > 0:                                    
    count -= 1                                     
    
    nhtml = urlopen(url, context = ctx).read()      # Atualizando a pagina atual do programa.
    html = BeautifulSoup(nhtml, 'html.parser')      # "Limpando" o codigo HTML.

    atags = html('a')                               # Extraindo todos os elementos ancora da pagina.

    pst_count = 0                                   # Zerando a contagem de posicoes dos links.

    for atag in atags:
        pst_count += 1                              # A cada ancora, a posicao se atualiza.

        if pst_count == pst:
            url = atag.get('href', None)            # Quando a posicao do usuario eh atingida, a nova URL eh extraida.
            print(re.findall('by_(.+)\.html', url)) # Assim como o nome contido nesse link.
            break
