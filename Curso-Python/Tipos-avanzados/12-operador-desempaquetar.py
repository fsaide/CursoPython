lista1 = [1, 2, 3, 4]
print(*lista1) #imprime de forma desempaquetada

lista2 = [5, 6]

combinado = [*lista1, *lista2] #combina 2 listas
print(*combinado)

coordenada1 = { "x" : 19 }
coordenada2 = { "y" : 15 }
nuevoPunto = {**coordenada1, **coordenada2, "z" : 4}
print(nuevoPunto)
