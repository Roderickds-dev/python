"""
el usuario ingresa un texto completo (primer input) (pasar a minus)
el usuario ingresa 3 letras (2do input) (pasar a minus)
retornaa al usuario lo siguiente
1) cuantas veces aparece c/letra que ingreso en el 2do input en el texto que ingreso en el 1er input
(alamacenas en una lista,
un metodo que permita contar cuantas aparece un sub dentro del string
(toupper))
2)Cuantas palabras en total hay dentro del texto que ingreso en el 1er input (convertir a list y count)
3)Primera letra y la ultima del texto que ingreso en el 1er input (index)
4)palabras en orden inverso (invertir el orden de la lista y otro que permita unir con espacios intermedios¿?)
5) python aparece dentro del texto? (booleanos para averiguar si aparece y diccionario para dar la respuesta)

"""

#Almacenamos las letras que ingresa el usuario y las pasamos a min
letras = (input('Ingresa tú primera letra: ').lower(),
          input('Ingresa tu segunda letra: ').lower(),
          input('Ingresa tu tercera letra: ').lower())
letra_1, letra_2, letra_3 = letras

#Recibimos el texto que ingresa el usuario
input_text = input('Ingresa un texto de tu agrado: ')

#Quitamos los caracteres especiales(Se debe hacer un exp-reg)
user_text = input_text.replace(",", "").replace(".", "").replace("!", "").replace("¡", "").replace("¿", "").replace("?", "").replace("??", "")

#Pasamos el texto a min
user_text = user_text.lower()

#Obtenemos la cantidad de veces que se repiten las letras que ingresa el usuario en el texto
first_letter = user_text.count(letra_1)
second_letter = user_text.count(letra_2)
third_letter = user_text.count(letra_3)

#Contamos la cantidad de palabras que contiene el texto
total_letters = len(user_text.split())

#Obtenemos la primera letra y la ultima
first_letter_text = user_text[0]
last_letter_text = user_text[-1]

#Texto inverso
#1era forma
reverse_text = user_text.split()[::-1]
reverse_text = " ".join(reverse_text)
#2da forma
palabras = user_text.split()
palabras.reverse()
rever_text_2 = ' '.join(palabras)

#Verificamos si esta dentro del texto python
python_var = "python"
python_inside = user_text.split()
python_inside = python_var in python_inside
dicc = {True: "si contiene la palabra python", False: "no contiene la palabra python"}
exists_python_in_text = dicc[python_inside]

print(f"""
          La letra '{letra_1}', aparece: '{first_letter}' veces en tú texto. 
          La letra '{letra_2}', aparece: '{second_letter}' veces en tú texto.
          la letra '{letra_3}', aparece: '{third_letter}' veces en tú texto.
          Tú texto contiene: '{total_letters}' palabras.
          La primera letra de tú texto es: '{first_letter_text}'.
          La última letra de tú texto es: '{last_letter_text}'.
          Asi se ve tu texto con el orden de las palabras invertidas: 
          '{reverse_text}'.
          Y por último, tu texto {exists_python_in_text} 
    """)


#print(dicc[falso])