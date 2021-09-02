'''
Programa que utiliza o algoritmo Merge Sort, retirado do livro "Introduction to Algorithms" para ordenar uma sequência aleatória de números em Python.
Myke Leony dos Santos Amorim. 01 de setembro de 2021.
Introdução à Análise de Algoritmos - Sistemas de Informação: USP.
'''

import sys
import random

def criar_vetor(tamanho):
    # Cria um vetor de tamanho especificado com n números inteiros aleatórios entre 0 e 100:
    vetor = list()

    for numero in range(tamanho):
        vetor.append(random.choice(range(100)))

    return vetor

def merge_sort (vetornumeros):
    print("Separando", vetornumeros)

    if len(vetornumeros) > 1:
        meio = len(vetornumeros)//2     # O operador piso (//) é necessário para evitar o retorno de pontos flutuantes.

        L = vetornumeros[:meio]         # Metade esquerda do vetor.
        R = vetornumeros[meio:]         # Metade direita do vetor.

        # Utilizando recursividade para separar todas as metades possíveis do vetor:
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Ordenando os números dentro dos vetores:
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                vetornumeros[k] = L[i]
                i += 1

            else:
                vetornumeros[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            vetornumeros [k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            vetornumeros[k] = R[j]
            j += 1
            k += 1

    print("Intercalando ", vetornumeros)

if __name__ == '__main__':
    # Testagem de exemplos:
    tamanho = 10
    exemplo = criar_vetor(tamanho)

    merge_sort(exemplo)

    print(exemplo)
