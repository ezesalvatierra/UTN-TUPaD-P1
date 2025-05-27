# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# - Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# - Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# - Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("¿Como quiere su nombre?")
print("1) En mayúsculas")
print("2) En minúsculas")
print("3) La primera letra mayúscula y el resto en minúsculas")
opcion = input("Elige una opcion (1, 2 o 3): ").strip()

if opcion == "1":
    nombre = nombre.upper()
    print(nombre)
elif opcion == "2":
    nombre = nombre.lower()
    print(nombre)
elif opcion == "3":
    nombre = nombre.title()
    print(nombre)
else:
    print("Opcion invalida. Por favor ingrese una opcion valida")