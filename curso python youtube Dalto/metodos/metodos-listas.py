#creando una lista con list()
lista = list(["hola", "kordit", 43])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando elementos a la lista con append
lista.append("jajajaja")

#agregando elementos a la lista en un indice especifico
lista.insert(2,"hola maquina")

#agregando varios elementos a la lista con extend
lista.extend(["zurvo",True])

#elemina un elemento de la lista por su indice
lista.pop(3) #(-1) para eliminar el ultimo, (-2) para eliminar el penultimo y asi sucesivamente

#removiendo un elelmento de la lista por su valor
lista.remove("hola maquina")

#elimina todos los elementos de la lista
#lista.clear()

#ordena la lista de menor a mayor (solo valores numericos)
#lista.sort()

#ordena la lista en reversa de mayor a menor (solo valores numericos)
#lista.sort(reverse = True)

#ordena los elementos de una lista
lista.reverse()

print (lista)
 