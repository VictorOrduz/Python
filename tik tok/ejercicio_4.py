'''haz una funcion que invierta cada palabra de una frase
Hola MUNDO --> aloH ODNUM'''

def invertido(frase):
    palabras = frase.split(" ")
    invertidas = []
    for palabra in palabras:
        invertidas.append(palabra[::-1])

    return " ".join(invertidas)

print(invertido("Hola MUNDO"))
