class Puerta:
    abierta = True
    material = "Madera"
    alto = 200
    ancho = 10
    largo = 100
    
    def __init__(self, abierta, material):
        self.abierta = abierta
        self.material = material
    
    def volumen(self):
        return self.alto * self.ancho * self.largo
    

puerta = Puerta(False, "acero")

print(puerta.abierta)
print(puerta.material)
print(puerta.volumen())