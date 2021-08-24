'''
Programa que utiliza a função format() para realizar truncamento.
Myke Leony dos Santos Amorim. 01 de maio de 2021.
'''

num = int(input())
wh = int(input())
aph = float(input())

salary = wh*aph

print('NUMBER =', num)
print('SALARY = U$ {:.2f}'.format(salary))
