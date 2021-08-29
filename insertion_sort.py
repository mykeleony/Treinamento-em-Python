'''
Programa que utiliza o algoritmo Insertion Sort, retirado do livro "Introduction to Algorithms" para ordenar uma sequência aleatória de números em Python.
Myke Leony dos Santos Amorim. 24 de agosto de 2021.
Introdução à Análise de Algoritmos - Sistemas de Informação: USP.
'''

lista_num = input('Insira os números (separados por espaços): ').split(' ')

vetor_a_ordenar = lista_num[1:]

for numero in vetor_a_ordenar:   # Iniciando o loop no a partir do segundo elemento.
    print(numero)
