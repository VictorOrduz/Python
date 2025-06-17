#creando diccionario con dict()
diccionario = dict(nombre = "kordit", apellido = "zurvo")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["kordit", "zurvo"]): "jajaja"}

#creando diccionaros con fromkeys(), valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionaros con fromkeys(), cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"], "no se")

print(diccionario)
