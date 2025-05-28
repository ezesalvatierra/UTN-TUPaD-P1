# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

cant_num = 10
sumatoria = 0

print("Ingresa", cant_num,"números enteros, al finalizar se mostrara la media de esos valores")

for i in range(cant_num):
    num_usuario = int(input(f"Ingresa el número {i+1}: "))
    sumatoria += num_usuario

media = sumatoria / cant_num
print("La media de los números ingresados es:",media)