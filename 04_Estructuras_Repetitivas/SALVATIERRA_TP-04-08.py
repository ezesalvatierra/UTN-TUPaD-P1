# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

cant_num = 100
pares = 0
impares = 0
positivos = 0
negativos = 0 

print("Ingresa", cant_num,"números enteros, al finalizar se mostrara la cantidad de números pares,impares,positivos y negativos.")

for i in range(cant_num):
    num = int(input(f"Ingrese el número {i+1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    else:
        negativos += 1

print("Cantidad de números pares:",pares)
print("Cantidad de números impares:",impares)
print("Cantidad de números positivos:",positivos)
print("Cantidad de números negativos:",negativos)