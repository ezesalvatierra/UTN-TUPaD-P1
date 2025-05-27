# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.

texto = input("Ingrese una palabla o frase: ")

if texto[-1] in ['a','e','i','o','u','A','E','I','O','U']:
    print(f"{texto}!")
else:
    print(texto)