'''
La droguería solo maneja 3 productos fijos en el sistema.
Cada uno tiene su propio nombre, precio e ingreso acumulado. 
El usuario podrá:
1. Ver los productos disponibles
2. Vender cualquiera de los 3 productos
3. Consultar ingresos totales
4. Salir del sistema
'''

producto1 = "acetaminofen"
precio1 = 2000
ingreso1 = 0

producto2 = "ibuprofeno"
precio2 = 3500
ingreso2 = 0

producto3 = "omeprazol"
precio3 = 6700
ingreso3 = 0

def mostrarMenu():
    print("\nMENU DROGUERIA")
    print("1. ver productos disponibles")
    print("2. vender producto")
    print("3. mostrar ingresos totales")
    print("4. salir")
    
def verProductos():
    print("\nPRODUCTOS DISPONIBLES")
    print(f"1. {producto1} - ${precio1}")
    print(f"1. {producto2} - ${precio2}")
    print(f"1. {producto3} - ${precio3}")
    
def venderProducto():
    global ingreso1, ingreso2, ingreso3
    verProductos()
    opcion = int(input("seleccione el numero del producto a vender: "))
    if opcion == 1:
        cantidad = int(input(f"¿cuantos {producto1} desea vender?: "))
        total = cantidad * precio1
        ingreso1 += total
        print(f"venta realizada por ${total}")
    elif opcion == 2:
        cantidad = int(input(f"¿cuantos {producto2} desea vender?: "))
        total = cantidad * precio2
        ingreso2 += total
        print(f"venta realizada por ${total}")
    elif opcion == 3:
        cantidad = int(input(f"¿cuantos {producto3} desea vender?: "))
        total = cantidad * precio3
        ingreso3 += total
        print(f"venta realizada por ${total}")
    else:
        print("opcion invalida")

def mostrarIngresos():
    totalIngresos = ingreso1 + ingreso2 + ingreso3
    print(f"el total de ingresos es ${totalIngresos}")
    
while True:
    mostrarMenu()
    opcion = int(input("seleccine una opcion: "))
    if opcion == 1:
        verProductos()
    elif opcion == 2:
        venderProducto()
    elif opcion == 3:
        mostrarIngresos()
    elif opcion == 4:
        print("saliendo del sistema")
        break
    else:
        print("funcion no valida")
        
