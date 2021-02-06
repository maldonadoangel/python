class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return print("El area del rectangulo es:", self.base*self.altura)

baseRectangulo = int(input("Ingrese la base del rectangulo: "))
alturaRectangulo = int(input("Ingrese la altura del rectangulo: "))

rectangulo = Rectangulo(baseRectangulo, alturaRectangulo)

print(rectangulo.area())