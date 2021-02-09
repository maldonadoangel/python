class Persona:
    def __init__(self, nombre, edad, dpi):
        self.__nombre = nombre
        self.__edad = edad
        self.__dpi = dpi
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    def get_dpi(self):
        return self.__dpi
    def set_dpi(self, dpi):
        self.__dpi = dpi

persona1 = Persona("Angel", 23, 2988166440101)
print(persona1.get_nombre(),"Tu edad es:", persona1.get_edad(),"Tu numero de dpi es:", persona1.get_dpi())