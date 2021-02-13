class Mascotas:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color
    
    def __str__(self):
        return "Tipo de mascota: " + self.tipo + ", Color: " + self.color

class Perro(Mascotas):
    def __init__(self, tipo, color, raza, tamanio):
        #Iniciamos los atributos de la clase padre a traves de el metodo super
        super().__init__(tipo, color)
        self.raza = raza
        self.tamanio = tamanio
        
    def __str__(self):
        return super().__str__() + ", raza de la mascota: " + self.raza + ", El tamaño es: " + self.tamanio

class Gato(Mascotas):
    def __init__(self, tipo, color, edad, raza):
        #Iniciamos los atributos de la clase padre
        super().__init__(tipo, color)
        self.edad = edad
        self.raza = raza
    
    def __str__(self):
        return super().__str__() + "La edad del minino es: " + self.edad + ", La raza es: " + self.raza

mascota = Mascotas("Gato", "Naranja")
print(mascota)

perro = Perro("Perro", "blanco", "Huskey", "grande")
print(perro)

gato = Gato("Gato", "Naranja", "8 meses", "Meztisa")
print(gato)