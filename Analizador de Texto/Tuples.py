"""Ocupan menos espacio en memoria lo que quiere decir que
se procesan mas rapido que las listas, estos son inmutables
son a prebas de daños (porque no se puden modificar)"""
palabra = "Un texto cualquiera"
palabra = palabra.split()
palabra.reverse()
palabra_al_reves = " ".join(palabra)
print(palabra_al_reves)
mi_tuple = (1,2,3,4, {"a": 2}, ["banana_split"], (1,2,1))
print(type(mi_tuple))
#Esto se llama casting transformar un tipo a otro
mi_tuple = list(mi_tuple)
print(type(mi_tuple))

"""Tanto con listas como con los diccionarios ponemos asignar los valores
de cada posicion a una varaible de la siguiente forma siempre tienen
que coincides la cantidad de elementos con la cantidad de variables"""
a,b,c,d,e,f,g = mi_tuple
print(e)

#Los tuples tienen 2 metodos index y count
"""Count te pide un parametro y es el elemento que quieres contar dentro
del tuple (saber cuantas veces esta ese valor dentro)"""
print(g.count(1))

"""el index() te duelve en que posicion se encuentra el elemento que 
quieres consultar, logicamente recibe como parametro dicho elemento"""

print(g.index(2))