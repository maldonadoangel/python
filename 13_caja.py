class Caja:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
    
    def base_caja(self):
        return self.alto * self.ancho * self.largo

    
alto_caja = int(input("Ingrese el alto de su caja: "))
ancho_caja = int(input("Ingrese el ancho de su caja: "))
largo_caja = int(input("Ingrese el largo de su caja: "))

cajas = Caja(alto_caja, ancho_caja, largo_caja)

print(cajas.base_caja()) 