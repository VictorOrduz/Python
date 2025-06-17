#funcion basica   
def saludar():
    print("hola")
    
saludar()

#funcion con parametros
def saludar_estudiante(nombre):
    print(f"hola {nombre} bienvenido")
    
saludar_estudiante("Melissa")

#funciones con retorno de valor
def sumar(num1, num2):
    return num1 + num2

resultado = sumar(10, 8)
print(resultado)

def sumahasta100():
    total = 0
    for i in range(1, 101):
        total += 1
    return total

print(f"la suma de 1 a 100 es {sumahasta100()}")
