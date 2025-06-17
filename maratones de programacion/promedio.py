for estudiante in range (9):
    nombre = input("ingrese el nombre del estudiante: ")
    nota1 = int(input("ingrese la primera nota: "))
    nota2 = int(input("ingrese la segunda nota: "))
    nota3 = int(input("ingrese la tercera nota: "))
    total = (nota1 + nota2 + nota3)/3
    
    if total >= 3.0:
        print(f"el estudiante {nombre} obtuvo una nota de {total} y aprueba")
    else:
        print(f"el estudiante {nombre} obtuvo una nota de {total} y no aprueba")
