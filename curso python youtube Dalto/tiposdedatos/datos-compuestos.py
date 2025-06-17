
#creando una lista (se puede modificar)
lista = ["kordit zurvo","I am viktor",True,1.70]

#creando una tupla (no se puede modificar)
tupla = ("kordit zurvo","I am viktor",True,1.70)

#esto es valido
lista [3] = "maquinola"

#esto no es valido
#tupla (3)

#creando un conjunto (set) (no se accede a elementos por indice) (no almacena datos duplicados)

conjunto = {"kordit zurvo","I am viktor",True,1.70,"I am victor"}

#print (conjunto[3]) -> no puede acceder al elemento

#creando un diccionario (dict)
diccionario = {
    'nombre' : "kordit zurvo",
    'quien soy' : "I am viktor",
    'esta emocionado' : True,
    'altura' : 1.70,
    'dato repetido' : "I am viktor"
}

print(diccionario['altura'])
print(lista[3])