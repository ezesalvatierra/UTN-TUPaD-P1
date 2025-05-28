# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

num_random = random.randint(0,9)
num_usuario = 10
cont = 0

print("Ingrese números del 0 al 9 hasta adivinar el número aleatorio")
while num_usuario != num_random:
    num_usuario = int(input(f"Intento N°{cont+1}: "))
    cont +=1
print("¡Acertaste!, lo hiciste en",cont,"intento/s")