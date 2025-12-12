#Enumerate sirve para acceder a los indices de una colección
#Como se haria sin enumerate
lista = ["a","b","c"]
indice = 0

for item in lista:
    print(indice, item)
    indice += 1

#Devuelve unos tuples
for item in enumerate(lista):
    print(item)

#Podemos separar el indice de la siguiente manera
for indice, item in enumerate(lista):
    print(indice, item)

#Tambien se puede usar para castear
mi_cast = list(enumerate(lista))
print(mi_cast)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

string = "Python"
print(string[0])
lista_indices = list(enumerate(string))
print(lista_indices)

for indice, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(indice)

