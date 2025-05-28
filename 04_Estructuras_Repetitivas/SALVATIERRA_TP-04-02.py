# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

numero = int(input("Ingrese un número entero: "))
cant_digitos = abs(len(str(numero)))

print("El número",numero,"tiene",cant_digitos,"digitos")