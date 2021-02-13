class Persona:
    def __init__(self, nombre, edad, dpi):
        self.nombre = nombre
        self.edad = edad
        self.dpi = dpi
    def __str__(self):
        return self.nombre + ", Edad: " + str(self.edad) + ", Dpi: " + self.dpi

