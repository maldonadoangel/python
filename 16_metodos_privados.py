class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno):
        self.nombre = nombre
        self._apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        
    def metodo_publico(self):
        self.__metodo_privado()
        
    def __metodo_privado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
        
        """ Creando el metodo get y set para el atributo privado """
    def get_apellido_materno(self):
        return self.__apellido_materno
    
    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

persona1 = Persona("Angel", "Morales", "Maldonado")

# persona1.__metodo_privado() No se puede acceder porque es privado

persona1.metodo_publico()

print(persona1.get_apellido_materno())
        
        
    