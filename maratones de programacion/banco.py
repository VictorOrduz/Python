opcion = ""

while opcion != 2:
    print("\n menu principal")
    print("1. proyectar capital con interes del 0.7% mensual")
    print("2. salir")
    
    opcion = input("seleccione una opcion: ")
    
    if opcion == "1":
        print("\n proyeccion de capital")
        capitalPrincipal = float(input("ingrese el capital inicial: "))
        meses = int(input("ingrese el numero de meses: "))
        
        tasa = 0.007
        
        capital = capitalPrincipal
        
        for mes in range(1, meses+1):
            capital = capital * (1+tasa)
            print(f"capital despues de {mes} mes ${capital:.2f}")
            
        print(f"capital final despues de {meses} meses ${capital:.2f}")
        
    elif opcion == "2":
        print("gracias por usar la aplicacion")
        break
    
    else:
        print("opcion no valida")
        
            