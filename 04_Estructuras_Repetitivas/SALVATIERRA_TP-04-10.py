# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_usuario = int(input("Ingrese un numero entero: "))
num_abs = abs(num_usuario)
num_invertido = 0
digito_actual = len(str(num_abs))-1

for i in range(len(str(num_usuario))):
    digito = num_abs % 10
    num_abs = int(num_abs / 10)
    num_invertido += digito * (10**digito_actual)
    digito_actual -= 1
    
if num_usuario < 0:
    num_invertido = int(num_invertido * -1)

print(num_invertido)