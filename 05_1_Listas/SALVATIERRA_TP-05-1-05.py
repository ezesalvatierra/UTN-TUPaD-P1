# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

# El programa va a eliminar el numero de mayor valor dentro del array utilizando el metodo remove para eliminar un elemento de la lista, 
# y la funcion max() para identificar el valor más alto. En este caso el numero de mayor valor es el 22, asi que la lista quedaria asi:
# [8,15,3,7]