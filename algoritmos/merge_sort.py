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
        meio = len(vetornumeros)//2

        L = vetornumeros[:meio]
        R = vetornumeros[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

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
    tamanho = 10
    exemplo = criar_vetor(tamanho)

    merge_sort(exemplo)

    print(exemplo)
