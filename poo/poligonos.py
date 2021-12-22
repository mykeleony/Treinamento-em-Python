class Poligono:
    def __init__ (self, nr_lados):
        self.n = nr_lados
        self.lados = [0 for i in range(nr_lados)]

    def le_lados (self):
        self.lados = [float(input('Insira o tamanho do lado '+str(i+1)+': ') for i in range(self.n))]

    def mostra_lados (self):
        for i in range (self.n):
            print('O lado', str(i+1), 'vale', self.lados[i])

class Triangulo:
    def __init__(self):
        Poligono.__init__(self, 3)

    def area(self):
        a, b, c = self.lados
        s = (a+b+c)/2   # Cálculo do semiperímetro
        area = (s*(s-a)*(s-b)*(s-c))**0.5

        print('A área do triângulo vale %0.2f ' %area)

# Testagens:
pentagono = Poligono(5)
