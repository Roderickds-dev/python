"""Sirve para encontrar valores mas bajos o mas altos en una colección funciona con valores numeros y alfabeticos
Cuando busca en strigs busca  primero en las mayusculas y luego en las minusculas"""
minimo = min(58, 96, 62, 30)
maximo = max(58, 96, 62, 30)
print(minimo, maximo)

lista_1 = [58, 96, 62, 30]
print(max(lista_1))

strings = ["Juan", "Roderick", "Jose"]
string2 = "Hola".lower()
print(max(strings), min(strings))

print(min(string2))

#En los diccionarios trae el valor de la clave que tiene el valor inferior .values() accedo a los valores
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
valor_maximo = max(lista_numeros)
valor_minimo = min(lista_numeros)
rango = valor_maximo - valor_minimo
print(rango)
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

#Con el values accedemos al valor del items es decir a la edad en este caso
edad_minima = min(diccionario_edades.values())
print(edad_minima)
#Por defecto aca siempre busca la clave es decir accede a los nombres en este caso
ultimo_nombre = max(diccionario_edades)
print(ultimo_nombre)
