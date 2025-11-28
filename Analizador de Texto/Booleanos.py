#Se escriben con la primera letra en mayuscula
verdadero = True
falso = False

#Tambien podemos usar el metodo bool() que retorna un boleano si se cumple la condicion
numero = bool(4<=4)
print(numero)

#Consultar si un valor esta dentro de una lista
mi_lista = [1,2,3]
esta = 4 in mi_lista
print(esta)
print(type(mi_lista))

palabra = "exito"
print(palabra[4])
print(palabra.index("o"))
