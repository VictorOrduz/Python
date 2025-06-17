#codigo para hallar porcentajes
porcentajes = [0.20, 0.30, 0.45, 0.05]

notas = []

for i in range(4):
    #entrada de datos por teclado
    nota = float(input(f"digite la nota {i+1}, (0-5): "))
    
    while nota < 0 or nota > 5:
        print("error la nota debe estar entre cero y cinco")
        nota = float(input(f"digite la nota {i+1}: (0-5) "))
        
    notas.append(nota)
    
#hallar el promedio
promedio = sum(notas[i] * porcentajes[i] for i in range(4))

if promedio < 3:
    print(f"como su promedio ha sido de {promedio}, por lo tanto REPROBO")
    
else:
    print(f"como su promedio ha sido de {promedio}, por lo tanto APROBO")
    
