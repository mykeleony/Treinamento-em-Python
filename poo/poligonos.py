class Poligono:
    def __init__ (self, nr_lados):
        self.n = nr_lados
        self.lados = [0 for i in range(nr_lados)]

    def le_lados (self):
        self.lados = [float(input('Insira o tamanho do lado '+str(i+1)+': ')) for i in range(self.n)]

    def mostra_lados (self):
        for i in range (self.n):
            print('O lado', str(i+1), 'vale', self.lados[i])

class Triangulo (Poligono):
    def __init__(self):
        Poligono.__init__(self, 3)

    def area(self):
        a, b, c = self.lados
        s = (a+b+c)/2   # Cálculo do semiperímetro
        area = (s*(s-a)*(s-b)*(s-c))**0.5

        print('A área do triângulo vale %0.2f unidades de área' %area)

class Retangulo (Poligono):
    def __init__ (self):
        Poligono.__init__(self, 4)

    def le_lados (self):
        l1 = float(input('Insira o tamanho do primeiro lado do retângulo: '))
        l2 = float(input('Insira o tamanho do segundo lado do retângulo: '))

        self.lados[0] = self.lados[2] = l1
        self.lados[1] = self.lados[3] = l2

    def area (self):
        area = self.lados[0] * self.lados[1]

        print('A área do retângulo vale %0.2f unidades de área' %area)

    def diagonal (self):
        diagonal = (self.lados[0]**2 + self.lados[1]**2)**0.5

def TrianguloRetangulo (Triangulo):
    def eh_triangulo_retangulo(self):
        return (self.lados[0]**2 == self.lados[1]**2+self.lados[2]**2 or self.lados[1]**2 == self.lados[0]**2+self.lados[2] or self.lados[2] == self.lados[0]**2+self.lados[1]**2)

# Testagens:
pentagono = Poligono(5)
pentagono.le_lados()
pentagono.mostra_lados()

triangulo = Triangulo()
triangulo.le_lados()
triangulo.area()

ret = Retangulo()
ret.le_lados()
ret.mostra_lados()
ret.area()
