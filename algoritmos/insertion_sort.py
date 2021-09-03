'''
Programa que utiliza o algoritmo Insertion Sort, retirado do livro "Introduction to Algorithms" para ordenar uma sequência aleatória de números em Python.
Myke Leony dos Santos Amorim. 25 de agosto de 2021.
Introdução à Análise de Algoritmos - Sistemas de Informação: USP.
'''

lista_num = input('Insira os números (separados por espaços): ').split(' ')

vetor = list(map(int, lista_num))

print('Números desordenados:', vetor)

for indice in range(1, len(vetor)):

     key = int(vetor[indice])
     posicao = indice

     while posicao > 0 and vetor[posicao-1] > key:
         vetor[posicao] = vetor[posicao-1]
         posicao = posicao-1

     vetor[posicao] = key

print('Números ordenados: ', vetor)
