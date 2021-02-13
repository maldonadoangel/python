class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "El vehiculo es color: " + self.color + " " + "Las ruedas del vehiculo son: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return super().__str__() + ", velocidad (km/hr): " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ", Tipo (Urbana/montaña/bmx): " + self.tipo
    

#Clase padre
vehiculo = Vehiculo("rojo", 4)
print(vehiculo)
    
#clase hija, coche
coche = Coche("Azul", 2, 150)
print(coche)

#clase hija, bicicleta
bicicleta = Bicicleta("Verde", 2, "BMX")
print(bicicleta)

        