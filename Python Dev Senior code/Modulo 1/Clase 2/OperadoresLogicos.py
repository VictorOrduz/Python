'''
Devsenior code en el examende certificacion internacional del modulo 4, pide que sus alumnos sean
calificados por 3 examenes, cada uno con un peso diferente
ca1: 30%
ca2: 40%
ca3: 30%
promedio:
0 - 2.9 - reprueba
3.0 - 5.0 - aprueba
mayor a 5 error
menor a 0 error
'''

ca1 = float(input("digite la calificaion 1: "))
ca2 = float(input("digite la calificaion 2: "))
ca3 = float(input("digite la calificaion 3: "))

ca1 *= 0.3
ca2 *= 0.4
ca3 *= 0.3

promedio = ca1 + ca2 + ca3

if promedio >= 0 and promedio < 3:
    print(f" el promedio es {promedio}, por lo tanto reprueba")
elif promedio >= 3 and promedio <= 5:
    print(f" el promedio es {promedio}, por lo tanto aprueba")
else:
    print("error")