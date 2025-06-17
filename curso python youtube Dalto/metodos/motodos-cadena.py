cadena1 = "soy,Kordit,Zurvo"
cadena2 = "bienvenido"

#print(dir(cadena1))

#convierte a mayusculas
mayuscula = cadena1.upper()

#convierte a minusculas
minuscula = cadena1.lower()

#convierte la primera letra en mayuscula
primera_letra_mayuscula = cadena1.capitalize()

#buscamos una cadena dentro de otra cadena, si no hay coincidencias, devuelve -1
busqueda_find = cadena1.find('R')

#buscamos una cadena dentro de otra cadena, si no hay coincidencias, lanza una excepcion
busqueda_index = cadena1.index('r')

#si es numerico devuelve true, sino devuelve false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true, si no devuelve false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es si devuelve True
empieza_con = cadena1.startswith("s")

#verificamos si una cadena termina con otra cadena dada, si es si devuelve True
termina_con = cadena1.endswith("o")

#reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("Kor","Rok")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[0])
