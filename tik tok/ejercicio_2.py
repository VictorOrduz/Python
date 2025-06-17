#desafio: verificar si una lista está ordenada de mecor a mayor

lista = [1, 2, 3, 4, 5]

ordenada = True

for i in range(len(lista)-1):
    if lista[i] > lista [i+1]:
        ordenada = False
        break
    
print(ordenada)
