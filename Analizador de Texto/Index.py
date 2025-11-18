my_text = "Hi world"

#Metodo index para buscar subcadenas dentro de un string
result = my_text.index("i")

#Metodo para buscar el valor de un indice especifico dentro de un string
result1 = my_text[0]
#print(result1)

"""Metodo rindex() busca de derecha a izquierda
Pero te retorna el valor del indice que corresponde
contando de izq a der
"""
result2 = my_text.rindex("l")
print(result2)