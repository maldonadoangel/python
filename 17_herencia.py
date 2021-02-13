class Persona:
    def __init__(self, nombre, dpi, edad):
        self.nombre = nombre
        self.dpi = dpi
        self.edad = edad
    def __str__(self):
        return "Nombre: " + self.nombre + ", Numero de dpi: " + self.dpi + ", Edad: " + str(self.edad)
        
class Empleado(Persona):
    def __init__(self, nombre, dpi, edad, sueldo):
        super().__init__(nombre, dpi, edad) #Con el super() accedemos a los atributos de la clase padre
        self.sueldo = sueldo
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)
        
persona = Persona("Juan", "2988166440101", 23)
print(persona)

empleado = Empleado("Angel", "4546564", 23, 5000.00)
print(empleado)
    
    