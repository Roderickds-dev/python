"""texto = "Tengo un texto cualquiera"
cualquiera= "cualquiera"
if not("texto" in texto):
    print("Esta dentro")
elif cualquiera in texto:
    print(f"{cualquiera} esta dentro")
else:
    print("No esta dentro")

edad = 19
calificacion = 10
if edad > 18:
    print("Eres mayor de edad")
    if calificacion > 8:
        print("Aprobaste")
    else: print("Reprobaste")
else: print("No eres mayor de edad")
"""

edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

if edad > 18 and tiene_licencia == True:
    print("Puedes conducir")
elif edad > 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

habla_ingles = False
sabe_python = True

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and not sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")

elif not sabe_python and habla_ingles:
    print("Para postularte, necesitas saber programar en Python")
