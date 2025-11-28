my_lyst = ['a','b','c']

#longitud de la lista
resultado = len(my_lyst)

#indice
resultado2 = my_lyst[1:]

#agregar un elemento
my_lyst.append('d')

"""Saltar un elemento (remover) si lo dejas vacio elimina el ultimo elemento
Puede almacenarse en un variable para su utilización"""
eliminado = my_lyst.pop(0)
print(eliminado, type(eliminado))

#Modificar un elemento de una lista
my_lyst[0] = "Alfa"
print(my_lyst)

#Ordernar lista este no devuelve nada no se puede almacenar en una variable
my_list2 = [1,9,2,18,3]
my_list2.sort() #NoneType es el resultado de un obj que no devuelve nada'
print(my_list2)

#Inversor del orden (desordenar)
my_list2.reverse()
print(my_list2)


