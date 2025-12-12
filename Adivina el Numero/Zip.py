"""Zip combina 2 o mas listas entrelanzando sus elementos en un tuple llega hasta el largo de la lista mas corta
dado que si tienes diferentes indices no hara nada"""
nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42]
ciudades = ["Lanus", "Quilmes","Florencio Valera"]
combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
frase = list(zip(paises, capitales))

for pais, capital in frase:
    print(f"La capital de {pais} es {capital}")

"""Crea el zip con las traducciones los números del 1 al 5 en español, 
portugués e inglés (en el mismo orden), y convierte el objeto 
generado en una lista almacenada en la 
variable numeros: 
uno / um / one dos / dois / two tres / três / three cuatro / quatro / four cinco / cinco / five 
El resultado deberá seguir la 
estructura: [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]"""

es = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
pt = ['um', 'dois', 'três', 'quatro', 'cinco']
en = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(es, pt, en))

print(numeros)