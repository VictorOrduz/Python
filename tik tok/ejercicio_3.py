#desafio: crear un diccionario con letras y su cantidad en un texto

texto = "banana"

frecuencias = {}

for letra in texto:
    if letra in frecuencias:
        frecuencias[letra] += 1
    else:
        frecuencias[letra] = 1
        
print(frecuencias)
