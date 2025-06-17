'''
Solicita el nombre de una ciudad y la temperatura actual,
luego muestra si hace frío (≤18°C), calor (≥30°C) o clima templado.
'''
ciudad = input("digite el nombre de la ciudad: ")
temperatura = float(input(f"digite la temperatura de la ciudad {ciudad}: "))

if temperatura <= 18:
    print(f"la ciudad {ciudad} es de clima frio")
elif temperatura > 18 and temperatura < 30:
    print(f"la ciudad {ciudad} es de clima templado")
else:
    print(f"la ciudad {ciudad} es de clima caliente")
