# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo!")
print("-------------------------------")
print("-------------------------------")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. 

nombre = input("Ingrese su nombre: ")
print("-----")
print(f"Hola {nombre}!")
print("-------------------------------")
print("-------------------------------")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print("-----")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
print("-------------------------------")
print("-------------------------------")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

radio = float(input("Ingrese el radio del circulo: "))
pi = 3.14159
perimetro = 2 * pi * radio
area = pi * (radio**2)
print("-----")
print(f"El perimetro del círculo es: {perimetro}")
print(f"El área del círculo es: {area}")
print("-------------------------------")
print("-------------------------------")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale. 

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = round(segundos / 3600, 2)
print("-----")
print(f"{segundos} segundos equivale a {horas} horas")
print("-------------------------------")
print("-------------------------------")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.

numero = int(input("Ingrese un número: "))
print("-----")
print(f"""Tabla de multiplicar del {numero}
{numero} * 1 = {numero * 1}
{numero} * 2 = {numero * 2}
{numero} * 3 = {numero * 3}
{numero} * 4 = {numero * 4}
{numero} * 5 = {numero * 5}
{numero} * 6 = {numero * 6}
{numero} * 7 = {numero * 7}
{numero} * 8 = {numero * 8}
{numero} * 9 = {numero * 9}
{numero} * 10 = {numero * 10}""")
print("-------------------------------")
print("-------------------------------")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

while True:
    num1 = int(input("Ingrese el primer número (distinto de 0): "))
    num2 = int(input("Ingrese el segundo número (distinto de 0): "))
    if num1 != 0 and num2 != 0:
        break
    else:
        print("Error: Ambos números deben ser distintos de 0. Intenta nuevamente.")
print("-----")
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = round(num1 / num2, 2)
print(f"Resultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print("-------------------------------")
print("-------------------------------")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal.

altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso (en kilogramos): "))
print("-----")
imc = peso / (altura**2)
print(f"Su índice de masa corporal es: {imc}")
print("-------------------------------")
print("-------------------------------")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit.

celcius = float(input("Ingrese la temperatura en grados Celcius: "))
print("-----")
fahrenheit = round((9/5) * celcius + 32, 2)
print(f"{celcius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")
print("-------------------------------")
print("-------------------------------")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = round((num1 + num2 + num3) / 3, 2)
print("-----")
print(f"El promedio es: {promedio}")
print("-------------------------------")
print("-------------------------------")