#declarar variables y pedir datos por teclado
edad = int(input("cual estu edad?: "))
salario = float(input("cual es tu salario?: "))
nombre = input("cual es tu nombre?: ")

#salida de datos por consola
print("la edad es:", edad)
print("el salario es: {}".format(salario))
print(f"el nombre es {nombre}")
print(f"el salario es {salario:.0f}")
