
print("AHORRO MEJORADO")
objetivo = float(input("¿cuanto dinero quieres ahorrar?: "))

while objetivo < 0:
    print("por favor escriba una cantidad positiva")
    objetivo = float(input("¿cuanto dinero quieres ahorrar?"))
    ahorrado = []
    while objetivo > ahorrado:
        ahorro = float(input("cuanto dinero quieres meter en tu plan de ahorro?"))
        while ahorro < 0:
            print("por favor escriba una cantidad positiva")
            ahorro = float(input("cuanto dinero quiere meter en el plan de ahorro?"))
        ahorrado += ahorro

print(f"¡objetivo conseguido! ha ahorrado usted {ahorrado} pesos")
