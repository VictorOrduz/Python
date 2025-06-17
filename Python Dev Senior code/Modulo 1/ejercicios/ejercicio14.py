'''
Pide el nombre de un proyecto y los días estimados de duración,
luego muestra cuántas semanas tomará (redondeando hacia arriba).
'''
proyecto = input("ingrese el nombre del proyecto: ")
dias = int(input("ingrese los dias de duracion del proyecto: "))

semana = dias / 7

print(f"el proyecto '{proyecto}' durará {semana:.0f} semanas")
