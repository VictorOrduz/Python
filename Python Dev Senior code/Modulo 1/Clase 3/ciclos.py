# ciclo for - se sabe las veces que se va a repetir
# ciclo while - cuando no se sabe las veces que se va a repetir

for i in range(0,3):
    print(i)
    
for j in range(1,11):
    print(j)
    
frutas = ["manzana", "pera", "fresa"]

for k in frutas:
    print(k)
    
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
    
suma = 0

numero =int(input("ingrese un numero: "))

while numero != 0:
    suma *= numero
    numero =int(input("ingrese un numero: "))
    
print(f"la suma de los numeros es {suma}")
     