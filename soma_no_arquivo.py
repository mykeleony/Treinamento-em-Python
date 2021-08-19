'''
28 de Junho de 2021.
Programa que usa expressões regulares para buscar todos os números contidos em um arquivo de texto e imprime a soma desses números.
Myke Leony dos Santos Amorim. 05 de maio de 2021.
'''

import re

nomearq = input('Enter file name: ')
arquivo = open(nomearq)   # Acessando os dados do arquivo nomeado pelo usuário. Nesse caso, o arquivo utilizado é o "actualdata.txt".

numeros = list()

for linha in arquivo:
    nums = re.findall('[0-9]+', linha)   # Para cada linha do arquivo, o programa busca um ou mais dígitos.

    for num in nums:
        nums.append(int(num))    # Em seguida, os números são armazenados em uma lista.

print(sum(nums))     # Imprimindo a soma dos números.
