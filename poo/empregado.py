'''
Sistema de folha de pagamento empresarial.

Myke Leony dos Santos Amorim. 22 de dezembro de 2021.
Curso de Laboratório de Programação Orientada a Objetos - USP.
'''

class Empregado:
    def __init__(self, nome, cpf, rg):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg

    def pagamento (self):
        print('O pagamento é um momento de grande felicidade para o funcionário!')

        return 0

class EmpregadoHorista (Empregado):
    def __init__(self, nome, cpf, rg, horas_trab, salario_hora):
        Empregado.__init__(self, nome, cpf, rg)
        self.horas_trab = horas_trab
        self.salario_hora = salario_hora

    def pagamento (self):
        return self.horas_trab * self.salario_hora

class EmpregadoCLT (Empregado):
    def __init__ (self, nome, cpf, rg, salario):
        Empregado.__init__(self, nome, cpf, rg)
        self.salario = salario

    def pagamento (self):
        return 13.3*self.salario
