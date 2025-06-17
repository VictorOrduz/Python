#pedir datos por consola
print("ingrese las notas del estudiante")
nota1 = float(input("primera nota: "))
nota2 = float(input("segunda nota: "))
nota3 = float(input("tercera nota: "))

#implementar operadores
nota1 *= 0.3
nota2 *= 0.3
nota3 *= 0.4

promedio = nota1 + nota2 + nota3

print(f"el promedio es {promedio:.2f}")
