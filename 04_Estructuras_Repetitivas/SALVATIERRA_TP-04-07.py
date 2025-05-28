# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

num = int(input("Ingrese un número entero positivo: "))
sumatoria = 0

if num > 0:
    for i in range(num):
        sumatoria += i
    print("La suma de todos los numeros enteros comprendidos entre 0 y",num,"es",sumatoria)
else:
    print("El número ingresado no es entero positivo")