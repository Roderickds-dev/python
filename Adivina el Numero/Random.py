"""Asi importamos randint de la libreria random de python
Si reemplazamos randint por un * trae toda la libreria random"""
from random import *
#Los valores que recibe esta funcion es el rango
aleatorio = randint(1, 50)


"""Metodo uniform() tira un valor aleatorio pero decimal (float) dentro del 
rango que elgimos, osea los parametros que le demos 
Lo metemos en un round() para poder especificar los decimales que 
queremos"""

aleatorio_2 = round(uniform(1, 5),3)
print(aleatorio_2)

"""metodo random() no lleva parametros porque elige un valor entre 0 y 1
 puede ser float o entero es decir 0 o 0.515 o 1 y asi"""

aleatorio_3 = random()
print(aleatorio_3)

"""choice te permite una seleccion aleatorio dentro de los elementos de una lista
los string tambien"""
colores = ["azul", "verde", "rojo", "negro"]
aleatorio_4 = choice(colores)
print(aleatorio_4)
string = "Roderick Zaragosa"
aleatorio_5 = choice(string)
print(aleatorio_5)

"""Shuffle es para mezclar va a a elegir lo que esta dentro de la lista pero los 
colocara con un orden distinto es un metodo que se usa en el lugar, no podemos almacenarlos
y tampoco lo podemos usar con strings porque son inmutables los string"""
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
