#decalarar variables y pedir datos por consola
producto1 = float(input("ingrese el valor del primer producto: "))
producto2 = float(input("ingrese el valor del segundo producto: "))
producto3 = float(input("ingrese el valor del tercer producto: "))

#aplicar operadores
total = producto1 + producto2 + producto3

total *= 0.65

print(f"el total a pagar es {total} USD")