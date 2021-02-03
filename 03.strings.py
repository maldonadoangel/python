string = '''
Esto es un string de multiples
lineas y esto esto


'''

print(string)
string = string.replace("esto", "aquello",2)
print(string)

#contar cuantas palabras se encuentran en el texto
print(string.count("o"))