"""Range es un funcion que te premite establecer un rango
de numeros sin necesidad de crear una lista o ni si
quiera un variable range(5) iterara desde 0-5 porque rango
comienza en 0 los 2 parametros 1ero es desde y 2do hasta el 3ero
son los pasos que va a salterse o sea de cada 2, solo integer
recibe

for x in range(0,50,10):
    print(x)"""

"""Si quisiereamos escribir una lista del 1-100
lista = list(range(0,101,10))
print(lista)"""

"""mi_lista = list(range(3,301,3))
print(mi_lista)"""
"""Utiliza la función range() y un loop para sumar los 
cuadrados de todos los números del 1 al 15 (inclusive).
Almacena el resultado en una variable llamada suma_cuadrados.

Para ello:

Crea un rango de valores que puedas recorrer en un loop

Para cada uno de estos valores, calcula su valor 
al cuadrado (potencia de 2). Puede que necesites crear 
variables intermedias (de manera opcional).

Suma todos los valores al cuadrado obtenidos. 
Acumula la suma en la variable suma_cuadrados."""

mi_lista = list(range(0,16))
suma_cuadrados = 0
for x in mi_lista:
   suma_cuadrados += x**2

print(suma_cuadrados)




