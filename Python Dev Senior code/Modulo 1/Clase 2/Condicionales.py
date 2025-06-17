'''
if(condicion):
    instrucciones
elif(condicion):
    instrucciones
else:
    instrucciones
'''

numero = int(input("digite el numero"))

#tomar decisiones (condicionales) - estructuras de control
if numero == 0:
    print(f"el {numero} es nulo")
elif numero > 0:
    print(f"el {numero} es positivo")
else:
    print(f"el {numero} es negativo")    
