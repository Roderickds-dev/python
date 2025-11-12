"""
Comisiones son del 13% el programa pregunta el numero y cuanto han vendido y el programa va a devolver
Ok juan. este mes ganas $650 cuanto_vendio = numero_ingresado * 13 /100 redondear con 2 decimales organizar
todo en un string para formatear
"""

nombre_vendedor = input("Ingrese su nombre: ")
cuanto_vendio = int(input("Ingrese el monto de sus ventas: $"))

total_comisiones = round(0.13 * cuanto_vendio, 2)
print(f"Ok. {nombre_vendedor}. Este mes ganaste ${total_comisiones}")

