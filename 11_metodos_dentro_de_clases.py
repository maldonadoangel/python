class Aritmetica:
    """Clase aritmetica para realizar sumas, restas, division etc..."""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def suma(self):
        """Se realiza la operacion con los atributos de la clase"""
        return self.operando1 + self.operando2
    def resta(self):
        return self.operando1 - self.operando2

#Creamos un objeto 
aritmetica = Aritmetica(5, 5)

print('Resultado es: ', aritmetica.suma())
print('Resultado de la resta:', aritmetica.resta())
        
        