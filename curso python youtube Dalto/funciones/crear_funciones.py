#creando una funcion simple
def saludar():
    print("hola kordit, hermano, como te va")

#ejecutando la funcion simple    
saludar()

#creando una funcion con parametros
def saludo(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    
    elif sexo == "hombre":
        adjetivo = "titan"
        
    else:
        adjetivo = "crack"
        
    print(f"hola {nombre}, mi {adjetivo}, ¿como estas?")
    
saludo("camila","mujer")
saludo("kordit","hombre")
saludo("fran","no-binario")

#crear una contraseña que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña
    
password = crear_contraseña_random(1)
frase = f"tu contraseña nueva es: {password}"
print(frase)

#crear una contraseña que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña,num

#desempaquetando la funcion    
password,primer_numero = crear_contraseña_random(165)
print(f"tu contraseña nueva es: {password}")
print(f"el numero usado para crarla fue el {primer_numero}")
