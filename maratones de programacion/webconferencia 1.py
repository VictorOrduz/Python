def calcular_area(base,altura):
    area = base * altura
    return area

def mostrar_area(area):
    print("el area del rectangulo es:", area)
    
base = int(input("escribe la base del rectangulo: "))
altura = int(input("escribe la altura del rectangulo: "))

resultado = calcular_area(base,altura)
mostrar_area(resultado)
