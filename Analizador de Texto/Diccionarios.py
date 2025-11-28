#diccioarios son type dict
#Podemos usar el in y el no in siempre y cuando busquemos la clave
persona = {"nombre": "Roderick", "apellido": "Díaz", "edad" : 31}
#print(persona["nombre"])
#Acceder a los valores dentro de un diccionario
cliente = {"nombre": "Juan",
           "celulares": [1122585274, 113974861],
           "ficha_medica":{"tipo_sangre": "A+", "alergias": "sulfa"}}
#print(cliente["celulares"][0])
#print(cliente["ficha_medica"]["tipo_sangre"])
#print( cliente["ficha_medica"]["alergias"].upper())

#Agregar elementos
celulares = cliente["celulares"]
persona["celulares"] = celulares
print(persona)

#Metodo keys() trae las clades esto es de tipo dict_keys
print(type(persona.keys()))

#Metodo values() trae los valores esto es de tipo dict_values
print(type(persona.values()))

#Trae los items que son tipo tuples
print(persona.items())




