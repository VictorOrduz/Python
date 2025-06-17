'''
Una empresa desea calcular el Retorno sobre la Inversión (ROI) y 
verificar si la inversión fue rentable (mayor a 1).
'''
ingresos = int(input("digite los ingresos de la empresa: "))
costo = int(input("digite el costo de la inversion: "))

roi = ((ingresos - costo) / (costo )) * 100

if roi >= 1:
    print(f"la inversion fue rentable, el roi fue de {roi:.2f}%")
else:
    print(f"la inversion no fue rentable, el roi fue de {roi:.2f}%")
   