#Los string son inmutables
nombre = "Carina"

#Concatenar
n1= "ro"
n2="derick"
print(n1+n2)

#Se pueden multiplicar los string
n3= "Roderick" #Esta salida RoderickRoderick
print(n3*2)

#Saltos de lineas (presionar enter) es como los comentarios
poema = """Hola
Esto es un 
poema"""
print(poema)

#Consulta un substring Deveulve true o false
print("es" in poema)
#tambien esta el not in que es el inverso
print("es" not in poema)
#Largo de un string len
print(len(poema))