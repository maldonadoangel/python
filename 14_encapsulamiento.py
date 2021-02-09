class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
   #get se utiliza para mostrar o retornar el valor de nuestro atributo
    def get_nombre(self):
       return self.__nombre
   #set para modificar el valor del atributo, ya que el encapsulamiento solo nos deja
   #trabajar de forma indirecta con los atributos y asi proteger la información
    def set_nombre(self, nombre):
        self.__nombre = nombre

        
p1 = Persona("Angel")
print(p1.get_nombre())
# print(p1.__nombre)  marca un error

p1.set_nombre("Hernan")
print(p1.get_nombre())

