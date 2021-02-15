from figura_geometrica import FiguraGeometrica
from cuadrado import Cuadrado


#No es posible crear objetos de una clase abstracta
# figurageo = FiguraGeometrica()

cuadrado = Cuadrado(5, "Azul")
print(cuadrado.area())
print(cuadrado.color())