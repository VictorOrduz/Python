contador = 100

while contador >= -100:
    print(contador)
    contador -= 10
    
print("fin del programa")

for i in range(0,4):
    print(i)
    
for letra in "python":
    print(letra, end = "")
    
print()

for letra in "python":
    if letra == "h":
        continue
    print(letra, end = "")  
      
#trabajando con menu de opciones
opcion = ""
contador = 0

while opcion != 3:
    print("menu de opciones:")
    print("1. saludar")
    print("2. despedirse")
    print("3. salir")
    
    opcion = input("ingrese la opcion: ")
    
    if opcion == "1":
        print("hola a todos")
    elif opcion == "2":
        print("hasta la proxima")
    elif opcion == "3":
        print("saliendo del sistema")
        break
    else:
        contador += 1
        print("opcion invalida")
        if contador == 3:
            print("has alcanzado el limite de 3 intentos, por lo tanto sales del sistema")
            break
        
    