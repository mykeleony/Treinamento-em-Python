'''
Programa que realiza manipulações elementares em ferramentas do pacote Natural Language ToolKit.
Myke Leony dos Santos Amorim. 15 de setembro de 2021.
Curso: Python para Processamento de Linguagem Natural - Instituto de Ciências Matemáticas e de Computação (USP).
'''

import nltk

nltk.download() # Para acessar algum corpus, é necessário baixá-lo previamente.

print(nltk.corpus.mac_morpho.words()) # Acessando o corpus de português brasileiro Mac-Morpho:
print('Este corpus possui '+str(len(nltk.corpus.mac_morpho.words()))+' palavras.')

print(nltk.corpus.mac_morpho.sents()[0]) # Acessando a primeira sentença do Mac-Morpho.
print(nltk.corpus.mac_morpho.tagged_words()) # Acessando as palavras com suas respectivas classes gramaticais em tuplas.
