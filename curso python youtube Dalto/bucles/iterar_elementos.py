animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,14,64,45]

#recorreindo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a {animal}")

#recorriendo la lista numeros y multiplicando por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#iterando 2 listas del mismo tamaño al mismo tiempo    
for numero,animal in zip(numeros,animales):
    print(f"recorriendo la lista 1: {numero}")
    print(f"recorriendo la lista 2: {animal}")

#iterando una lista con range()    
for num in range(5):
    print(num)
    
#forma no optima de recorrer una lista, (no funciona con conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es {indice}, y el valor es {valor}")

#usando el for/else
for numero in numeros:
    print(numero)
    
else:
    print("el bucle terminó")

#todo lo anterior funciona igual para tuplas y conjuntos