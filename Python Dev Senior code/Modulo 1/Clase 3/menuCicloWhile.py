saldo = 5.000

historial = []
suma_retiro = []
suma_deposito = []

login = "user"
clave = "1234"

contador = 0

while True:
    
    usuario = input("ingrese su usuario: ")
    contraseña = input("digite su clave: ")
    if usuario == login and contraseña == clave:
        
        while True:
            print("\n ----MENU----")
            print("1. Ver Saldo")
            print("2. Retirar Dinero")
            print("3. Depositar Dinero")
            print("4. Ver historial de movimientos")
            print("5. Cambiar clave")
            print("6. Salir")
            
            opcion = int(input("Digite la opcion: "))
            
            if opcion == 1:
                print(f"su saldo actual es: {saldo:.3f}")
                
            elif opcion == 2:
                retiro = float(input("cuanto deseas retirar? "))
                if retiro <= saldo:
                    saldo -= retiro
                    historial.append(f"Retiraste {retiro:.3f}")
                    suma_retiro.append(retiro) 
                    print(f"Retiro exitoso. Saldo restante ${saldo:.3f}")
                else:
                    print("Saldo insuficiente")
                    
            elif opcion == 3:
                monto = float(input("Cuanto quieres depositar? "))
                if monto > 0:
                    saldo += monto 
                    historial.append(f"Depositaste {monto:.3f}")
                    suma_deposito.append(monto)
                    print(f"Deposito exitoso el nuevo saldo es: {saldo:.3f}")
                else:
                    print("No puedes depositar montos negativos")
                    
            elif opcion == 4:
                print("Historial")
                if len(historial) == 0:
                    print("No tienes movimientos")
                else:
                    for movimiento in historial:
                        print(movimiento)
                        
                sum1 = sum(suma_retiro)
                print(f"el total de dinero retirado es {sum1:.3f}")
                    
                sum2 = sum(suma_deposito)
                print(f"el total del dinero depositado es {sum2:.3f}")
            
            elif opcion == 5:
                intento = input("escribe tu clave actual")
                if intento == clave:
                    nueva = input("Digita tu nueva clave: ")
                    clave = nueva 
                    print("Tu clave ha sido cambiada con exito ")                
                else:
                    print("Clave incorrecta.")
                    
            elif opcion == 6:
                print("gracias por usar nuestro sistema")
                break
            
            else:
                print("Opcion invalida")
                
        if opcion == 6:
            break
            
    else:
        contador += 1
        print("usuario o clave incorrecto")
        if contador == 3:
            print("has alcanzado el numero de intentos permitidos")
            break
                    