
frutas = ["banana","manzana","cereza","pera","mandarina","granadilla","durazno"]
cadena = 'hola Kordit'
numeros = [2,4,5,10]

#evitando que se coma una granadilla con la sentencia continue
for fruta in frutas:
    if fruta == "granadilla":
        continue
    print(f"me voy a comer una {fruta}")
        
#evitar que el bucle siga ejecutandose, (el else no se ejecuta tampoco)
for fruta in frutas:
    if fruta == "pera":
        break
    print(f"me voy a comer una {fruta}")  
    
else:
    print("terminado")
   
#recorriendo cadenas de texto    
for letra in cadena:
    print(letra)
    
#duplicando los numeros de una lista
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2)
    
print(numeros_duplicados)

#vamos a realizar el codigo anterior en 2 lineas de codigo
#for en una sola linea de codigo (duplicando los numeros)        
otros_numeros_duplicados = [x * 2 for x in numeros]
print(otros_numeros_duplicados)
