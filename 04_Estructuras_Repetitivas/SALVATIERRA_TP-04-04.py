#Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

sumatoria = 0
numero = 1

while numero != 0:
    numero = int(input("Ingrese un número entero para sumar (Ingrese 0 para detener la suma): "))
    sumatoria += numero

print('La suma de todos los números ingresados es',sumatoria)