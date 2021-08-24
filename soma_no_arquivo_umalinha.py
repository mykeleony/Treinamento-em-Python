'''
11 de maio de 2021.
Programa que usa expressões regulares e compreensão de lista para buscar todos os números contidos em um arquivo de texto e imprime a soma desses números.
'''

import re

print( sum( [int(n) for n in re.findall('[0-9]+', open('actualdata.txt').read()) ] ) )
