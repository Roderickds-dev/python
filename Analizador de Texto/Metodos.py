texto = "Este es el texto de Prueba"
#Metodo para escribir el texto a may
resultado = texto.upper()
#Metodo para escribir el texto en min
resultado2 = texto.lower()
"""Metodo split separa el texto y lo guarda dentro de una list (arr)
Por defecto toma como separador los espacios vacios
1ero parametro indica el criterio de separación
2do parametro determina cuantos elementos va a separar para hacer
la list (contando el 0)"""
resultado3 = texto.split(' ', 1)
#print(resultado3)

#Metodo join es para unir elementos de una lista.
lista1 = ["esta", "es", "una", "lista"]
a = "Roderick"
b = "esta aprendiendo"
c = "Python"
e = " ".join(lista1) #metodo1
d = "-".join([a,b,c]) #metodo2
print(e)

"""Metodo find busca un determinador caracter dentro del string
la diferencia con el metodo index es que esto si no encuentra el caracter
te retorna -1 y no un error"""

resultado4 = texto.find("e")
print(resultado4)

"""Metodo replace 1ero parametro lo que va a reemplazar y el 2do
el texto por el cual sera reemplazado"""

resultado5 = texto.replace("e","3")
print(resultado5)



