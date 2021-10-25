'''
Programa que realiza manipulações elementares no Natural Language ToolKit.
Myke Leony dos Santos Amorim. 15 de setembro de 2021.
Curso: Python para Processamento de Linguagem Natural - Instituto de Ciências Matemáticas e de Computação (USP).
'''

import nltk
import re

from nltk.tokenize import RegexpTokenizer

from nltk import ngrams

# nltk.download() -> Para acessar corpus, é necessário baixá-los previamente;

print('Utilizando o corpus (dataset de PLN) de português brasileiro Mac-Morpho:')
print('-------------------------------------------------------------------\n')

# Acessando o corpus de português brasileiro Mac-Morpho:
print('Palavras do corpus:', nltk.corpus.mac_morpho.words())
#print('Este corpus possui '+str(len(nltk.corpus.mac_morpho.words()))+' palavras.')

sentenca = nltk.corpus.mac_morpho.sents()[41] # Acessando a 41a sentença do Mac-Morpho.
sentenca = " ".join(sentenca) # Inserindo a primeira sentença do Mac-Morpho em uma string.

print('\n41a sentença do corpus:', sentenca)

print('\nPalavras do corpus etiquetadas com classes gramaticais:', nltk.corpus.mac_morpho.tagged_words()) # Acessando as palavras com suas respectivas classes gramaticais.

'''Tokenização (fragmentação sistemática de textos): '''
tokens_sentenca = nltk.word_tokenize(sentenca)

print('\nTokens (fragmentos) da 41a sentença: ',tokens_sentenca)

print('\n--------------------------------------------------------------------------------\n')

# Tokenização personalizada (com expressão regulares):
tokenizador1 = RegexpTokenizer(r'\w+')  # Ignorando pontuações (exceto o underscore _)

# Retirada de Stopwords (palavras irrelevantes à análise do corpus):
# A conversão das palavras para minúsculas é necessária para evitar a dispersão da frequência da mesma palavra em outras:
stopwords = nltk.corpus.stopwords.words('portuguese')
print('Palavras consideradas Stopwords (irrelevantes à análise do corpus) pelo NLTK:', stopwords)

tokens_sem_pontuacao_filtrados = [token.lower() for token in tokenizador1.tokenize(sentenca) if token not in stopwords]

tokenizador2 = RegexpTokenizer(r'[A-z]\w+') # Ignorando pontuações e números.
tokens_sem_pontuacao_e_num_filtrados = [token.lower() for token in tokenizador2.tokenize(sentenca) if token not in stopwords]

print('\nTokens sem pontuação filtrados (sem Stopwords):', tokens_sem_pontuacao_filtrados)
print('\nTokens sem pontuação e sem números:', tokens_sem_pontuacao_e_num_filtrados, '\n')

# Contagem/frequência de tokens:

frequencia = nltk.FreqDist(tokens_sem_pontuacao_filtrados)
print(frequencia)
print('Tokens (sem pontuação e sem Stopwords) mais comuns:',frequencia.most_common(3)) # "Top 3" tokens mais frequentes na 41a sentença do corpus Mac-Morpho. Sem o parâmetro, todos os tokens e suas ocorrências seriam mostrados.

# Obtenção de N-Gramas (palavras que ocorrem em conjunto):
exemplo = 'Myke Leony é lindo. Myke Leony é charmoso. Reinaldo Junior é corno. Ellen Silva também.'
tokens_exemplo = tokenizador1.tokenize(exemplo)

print("\n2-gramas do texto \'"+exemplo+"\':", list(ngrams(tokens_exemplo, 2)))
