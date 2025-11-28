"""Lo sets solo admiten elementos unicos, si un elemento se repite
python lo descarta automaticamente, no estan ordenados en indices,
son inmutables tambien, no puedes incluir listas ni diccionarios,
Admite tuples(porque son inmutables)"""

#Primera forma de escribirlo
mi_set= set([1,2,3,4,5])

#Segunda forma de escribirlo
second_set = {"a","b","c","d"}
print(mi_set, type(mi_set), type(second_set))

#Podemos consultar el largo
print(len(mi_set))

#Podemos verificar si un elemento esta dentro o no
print(2 in second_set)
print(3 not in second_set)

#Union de sets
tercer_set = mi_set.union(second_set)
print(tercer_set)

#Agregar elementos
tercer_set.add(15)
print(tercer_set)

"""Eliminar elementos remove() o discard() remove te da error si no encuentra
el elemento en cambio discard no te da error si no lo encuentra"""

tercer_set.remove(15)
tercer_set.discard(9)
print(tercer_set)

"""El pop() aca eliminar un elemento random y recordar que se puede almacenar
dicho elemento en una variable"""

#El clear() vacia el set
#second_set.clear()
set_pop = second_set.pop()
second_set.discard(set_pop)
print(second_set)