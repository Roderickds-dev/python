"""Aparte de elegir una opcion entre varias va a permitir
ejecutar algo en base a eso dentro del mismo match
el case _: es el break"""

edad = 17
match edad:
    case 18:
        print("Mayor de edad")
    case 17:
        print("Menor de edad")
    case _:
        print("Intruduzca una edad")

cliente = {"nombre" : "Roderick", "edad" : 31, "Ocupación": "Desarrollador"}
pelicula = {"titulo": "Fast 1", "ficha_tecnina": {
    'protagonista_1': "Bryan O'conner", "protagonista_2":"Toretto"
}}
elementos = [cliente, pelicula]
#Cuanod hacemos nombre, edad, ocupacion es asignar el valor que tenga dicha clave a ese variable, por eso despues la imprimos las variables
for e in elementos:
    match e:
        case {"nombre":nombre, "edad":edad, "Ocupación": ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo,
              "ficha_tecnina":{
              "protagonista_1":protagonista_1, "protagonista_2":protagonista_2}}:
            print("Es un pelicula")
            print(f"{titulo}, Protagonista 1: {protagonista_1}, Protagonista 2: {protagonista_2}")
        case _:
            print("No se que elemento es")

