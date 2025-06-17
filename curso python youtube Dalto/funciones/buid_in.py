numeros = (5, 16, 42, 1, 90)

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 2 decimales con round() y formula matematica
numero = round(12.345678 * 100)
print(numero / 100)

#redondeando a 2 decimales con round() eficazmente
numero = round(12.345678,2)
print(numero)

#retorna False -> 0, vacio, False, none \ retorna True -> distinto a cero, True, cadena, datos no vacios
resultado_bool = bool()
print(resultado_bool)

#retorna True si todos los valores son verdaderos
resultado_all = all([23,5,"True",[43,65]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)

