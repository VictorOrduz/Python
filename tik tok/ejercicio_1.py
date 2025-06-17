#desafio: contar cuantas palabras tienen mas de 5 letras

frase = "Python es un lenguaje genial para programar"

palabras = frase.split()
print(palabras)
contador = 0

for palabra in palabras:
    if len(palabra) > 5:
        contador += 1
         
print(contador)
