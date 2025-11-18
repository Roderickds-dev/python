texto = "abcdefghijklmn"
"""Seria como el metodo slice el primer parametro es desde
donde empieza hasta el 2do parametro sin incluirlo; si no colocamos
el primer parametro o el 2do parametro asume que es desde que
empiza o hasta donde termina, el 3er parametro indica cada cuanto
caracter voy a ir extayendo
"""
fragmento = texto[2:5]
#print(fragmento)

frase = "Controlar la complejidad es la esencia de la programación"
ext = frase[0:9]
#Esto invierte los caracteres frase[::-1]
print(ext)