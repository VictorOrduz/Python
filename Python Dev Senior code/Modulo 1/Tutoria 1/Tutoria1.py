a = 3
b = 4
c = a % b
print(c)

'''
determinar si un numero es par o impar y multiplicarlo si es impar
'''
num = int(input("digite un numero entero: "))

if num % 2 == 1:
    print(f"el numero {num} es impar")
    print(num * num)
elif num % 2 == 0: 
    print(f"el numero {num} es par")
else:
    print("digite un numero entero")
    