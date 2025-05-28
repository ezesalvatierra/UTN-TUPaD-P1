# Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
sumatoria = 0

if num1 > num2:
    for i in range(num2+1,num1):
        sumatoria += i
    print("La suma de todos los números enteros comprendidos entre",num2,"y",num1,"(excluyendolos) es",sumatoria)
elif num2 > num1:
    for i in range(num1+1,num2):
        sumatoria += i
    print("La suma de todos los números enteros comprendidos entre",num1,"y",num2,"(excluyendolos) es",sumatoria)
else:
    print("La suma de todos los números enteros comprendidos entre",num1,"y",num2,"(excluyendolos) es",sumatoria,"ya que ambos números son iguales")