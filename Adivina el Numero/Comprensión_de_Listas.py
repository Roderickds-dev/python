palabra = "Python"
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

#Como seria con comprension y como se lee
"""Quiero que la variable lista sea igual a una lista 
cada elemento va a ser una letra de cada letra que haya en palabra
los valores deben ser igual de la primera y segunda variable (letra = letra)"""

name = "Roderick"
name_list = [letra for letra in name]
#una letra por cada letra que haya en palabra
print(name_list)

#Ejemplo con mumero

numeros = range(0,15, 2)
"""De esta forma tomara los numeros y los dividira en 2
o sea que vamos alterar el valor antes de incluirlo en la lista
"""
lista_numeros = [numero / 2 for numero in numeros]
print(lista_numeros)

#Podemos hacer condiciones tambien
lista_numeros_2 = [n for n in numeros if n*2 > 10]
print(lista_numeros_2)

"""Si queremos incluir un else cambia la estructua asi"""
lista_numeros_3 = [n if n *2 >10 else "no cumple" for n in numeros]
print(lista_numeros_3)

#Otro ejemplo
pies = list(range(10,51, 10))
metros = [ round(p / 3.281,3) for p in pies]
print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]
print(valores_cuadrado)