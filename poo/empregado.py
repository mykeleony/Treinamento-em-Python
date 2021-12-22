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
