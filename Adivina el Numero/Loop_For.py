"""for se repiten durante una cantidad definida de repeticiones o iteracion
"""

lista_nombres = ["Ramón", "Luis", "Pedro"]
lista_de_objetos = [{"nombre":"Ramón", "edad": 18},{"nombre":"Luis", "edad": 16},{"nombre":"Pedro", "edad": 20}]
diccionario = {"name": "Roderick", "age": 31, "city" : "CABA"}

#La primera variable es la que asignameros el valor, es decir "por cada nombre en nombres" seria la traducción

for nombre in lista_nombres:
    numero_de_indice = lista_nombres.index(nombre) + 1
    print(f"{numero_de_indice}: {nombre}")

for objeto in lista_de_objetos:
    if objeto["edad"] >= 18:
        print(f"{objeto['nombre']}, es mayor de edad ")

#Asi podemos iterar un lista dentro de otra
list_1 = [[1,2],[3,4],[5,6]]
#Tenemos que la primera variable toma todos los valores en la posicion 0 dentro de la listas internas
for obj1,obj2 in list_1:
    print(obj1)

#Como podemos imprimir todos los elementos dentro de un dic
for item in diccionario.items():
    print(item)

lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
    elif numero % 2 == 1:
        suma_impares = suma_impares + numero

print(suma_pares, suma_impares)