mascotas =  [
    "scarface",
    "pelusa",
    "negra",
    "daysi",
    "chispa"
            ]

mascotas.insert(1, "pulga") #agrega en la posicion 1 de la lista
mascotas.append("nano") #agrega al final
print(mascotas)
print(" ")

mascotas.remove("chispa") #elimina el elemento (si esta repetido elimina el 1ro)
mascotas.pop(1) #elimina el elemento de esa posicion(si no tiene indice el ultimo)
del mascotas[0] #lo mismo que pop
print(mascotas)

mascotas.clear() #limpia la lista

#list.insert(index, element) -> agrega en el elemento en el indice indicado
#list.append() -> agrega al final
#list.pop(indice) -> elimina el indice indicado, de no tener indice elimina el ultimo
#list.remove(elemento) -> elimina el elemento indicado, de estar repetido elimina el 1ro
#del list[index] -> misma funcionalida que pop
#list.clear() -> elimina todos los elementos de la lista
