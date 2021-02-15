from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def area(self):
        print('Area')
        return self.get_alto() * self.get_ancho()
    
    def color(self):
        return "Color: " + self.get_color()
    
    