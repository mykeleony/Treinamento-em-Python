''' 
Exercício de fixação: arquitetura de uma classe para o tipo de objetos "Carro".
Myke Leony dos Santos Amorim. 22 de dezembro de 2021.
Curso de Laboratório de Programação Orientada a Objetos - USP.
'''

class Carro:
    def __init__(self, ano, modelo, cor, velMax):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
        self.velMax = velMax

    def imprima (self):
        if self.velocidade == 0:
            print('%s %d %s parado.' %(self.modelo, self.ano, self.cor))

        else:
            print('%s %s em movimento a %0.2f km/h.' %(self.modelo, self.cor, self.velocidade))

    def acelera (self, velocidade):
        if velocidade <= self.velMax:
            self.velocidade = velocidade

        else:
            self.velocidade = self.velMax

        self.imprima()

    def pare (self):
        self.velocidade = 0

        self.imprima()

def main ():
    # Testagens:
    meu_carro = Carro(2002, "Civic", "Roxo", 250)
    carro_usp = Carro(2021, "Lamborghini", "Preto", 300)

    meu_carro.imprima()
    carro_usp.imprima()

    carro_usp.ano -= 10     # Modificando atributos da instância.

    carro_usp.imprima()

    meu_carro.acelera(70)
    meu_carro.acelera(40)
    meu_carro.acelera(500)
    meu_carro.pare()

if __name__ == '__main__':
    main()
