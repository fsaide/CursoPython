#set es una coleccion de datos donde no se repiten elementos
#y tambien estan ordenados

primer = {5, 5, 2, 2, 3, 3, 4, 4}
print(primer)
print("")

primer.add(1) #agrega 1 al set
primer.remove(5) #elimina 5 del set
print(primer)
print(" ")

segundo = [3, 4, 5]
segundo = set(segundo) #pasa de lista a set
print(segundo)
print("")
print(primer | segundo) #imprime 1er y 2do combinando ambas listas 
print("")
# | = union



print(primer &  segundo ) #imprime 1er y 2do intersecando ambas listas
print("")
# & = interseccion

print(primer - segundo) #imprime 1er menos la diferencia del 2do
print("")
# - = diferencia

print(primer ^ segundo) #imprime lo q esten en 1er y 2do pero no en ambos
print("")
# ^ = diferencia simetrica

#no podemos acceder a los elementos de los sets
#pero si podemos consultarlos


