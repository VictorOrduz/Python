diccionario = {
    "nombre" : 'kordit',
    "apellido" : 'zurvo',
    "subs" : 1000000
}

#devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemneto con get(), si no encunetra nada el programa continua
valor_de_hdp = diccionario.get("hdp")
print("hola papa, el programa continua")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
