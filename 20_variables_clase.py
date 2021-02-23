class MiClase:
    # Es una variable definida fuera de cualquier metodo o funcion de nuestra clase
    #Pero siempre estando dentro de la clase 
    #La variable clase solo puede ser modificada de forma global por la clase
    
    variable_clase = "Variable de clase, sigo siendo el valor original, porque soy de tipo global dentro de la clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia    
        

print(MiClase.variable_clase)
objeto1 = MiClase("Variable Instancias")
print(objeto1.variable_instancia)#Valores distintos, esta variable se asocia con el objeto
#Podemos acceder a las variables de clase desde los objetos
print(objeto1.variable_clase)
#podemos acceder a las variables de clase desde la clase
print(MiClase.variable_clase)

#El objeto modifica la variable clase pero solo para ese objeto
#ya que si verificamos de nuevo el valor de la variable de clase
#seguira con su valor original
objeto1.variable_clase = "Modificando desde el objeto la variable de la clase pero solo veo el cambio en el objeto"
print(objeto1.variable_clase)
print(MiClase.variable_clase)