# Utilizando la información aportada tabla sobre las estaciones del año:
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hem = input("Ingrese en que hemisferio se encuentra (N (Norte) o S (Sur)): ").strip().lower()
mes = int(input("Ingrese el mes actual (1-12): "))
dia = int(input("Ingrese el dia de hoy: (1-31): "))

if hem == "n":
    if (mes == 12 and dia >= 21) or (1 <= mes < 3) or (mes == 3 and dia < 21):
        print("La estacion actual es: Invierno")
    elif (mes == 3 and dia >= 21) or (4 <= mes < 6) or (mes == 6 and dia < 21):
        print("La estacion actual es: Primavera")
    elif (mes == 6 and dia >= 21) or (7 <= mes < 9) or (mes == 9 and dia < 21):
        print("La estacion actual es: Verano")
    elif (mes == 9 and dia >= 21) or (10 <= mes < 12) or (mes == 12 and dia < 21):
        print("La estacion actual es: Otoño")
elif hem == "s":
    if (mes == 12 and dia >= 21) or (1 <= mes < 3) or (mes == 3 and dia < 21):
        print("La estacion actual es: Verano")
    elif (mes == 3 and dia >= 21) or (4 <= mes < 6) or (mes == 6 and dia < 21):
        print("La estacion actual es: Otoño")
    elif (mes == 6 and dia >= 21) or (7 <= mes < 9) or (mes == 9 and dia < 21):
        print("La estacion actual es: Invierno")
    elif (mes == 9 and dia >= 21) or (10 <= mes < 12) or (mes == 12 and dia < 21):
        print("La estacion actual es: Primavera")