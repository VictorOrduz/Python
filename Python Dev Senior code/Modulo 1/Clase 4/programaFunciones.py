def validarPass():
    password = "devsenior"
    intentos = 0
    
    while intentos < 3:
        entrada = input("ingrese el password: ")
        if entrada == password:
            print("bienvenido")
            return
        else:
            intentos += 1
            print(f"password incorrecto, tienes {3 - intentos} intentos")
    print("has excedido el numero de intentos")
    
validarPass()

