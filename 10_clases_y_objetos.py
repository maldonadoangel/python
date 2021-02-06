class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Modificar nombres
Persona.nombre = "Angel"
Persona.edad = 23

#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)


#creacion de un objeto

persona = Persona("Karla", 30)
print(persona.nombre)
print(persona.edad)
#Creacion de un segundo objeto

persona2 = Persona("Hernan", 43)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2))
print(id(persona))

    
    