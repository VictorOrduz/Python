#creando un conjunto con set()
conjunto = set(["Dato 1"])

#mtiendo un conjunto dentro de otro conjunto
conjunto_1 = frozenset(["dato 1", "dato 2"])
conjunto_2 = {conjunto_1, "dato 3"}
print(conjunto_2)

#teoria de conjuntos
conjunto_1 = {1,3,5,7}
conjunto_2 = {1,3,7}

#verificando si hay un subconjunto
resultado = conjunto_2.issubset(conjunto_1)
resultado = conjunto_2 <= conjunto_1

#verificando si hay un superconjunto
resultado = conjunto_1.issuperset(conjunto_2)
resultado = conjunto_1 > conjunto_2

#verificar si hay algun numero en comun
resultado = conjunto_2.isdisjoint(conjunto_1)

print(resultado)
