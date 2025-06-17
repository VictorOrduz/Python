numeros = []
def separar(x):
    while x > 0:
        print(x % 10)
        numeros.append(x % 10)
        x = x // 10
    print(numeros[:])

n = int(input("ingrese el codigo del libro de 6 digitos"))
separar (n)