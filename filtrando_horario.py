'''
10 de maio de 2021.
Programa que busca linhas contendo o horário de envio de e-mails, conta as ocorrências de cada hora e as imprime em ordem crescente.
'''

filename = input('Enter file name: ')
file = open(filename)

hour_count = dict()

for line in file:

    if line.startswith('From:') is True: continue

    elif line.startswith('From') is True:
        words = line.split()
        time_elements = words[5].split(':')
        hour = time_elements[0]
        hour_count[hour] = hour_count.get(hour, 0)+1

hours_sorted = sorted(hour_count.items())

for key,value in hours_sorted:
    print(key, value)
