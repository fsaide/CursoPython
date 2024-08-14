#una tupla es igual que una lista, la diferencia es que las tuplas no se pueden 
#modificar

numeros = (1, 2 ,3)
print(numeros)
numeros2 = (1, 2, 3) + (4, 5, 6)
print(numeros2)

punto = tuple([1, 2]) #pasa de una lista a una tupla
print(punto)

#una tupla no se puede modificar pero si se puede
#acceder a ellos con funciones que no la modifiquen

for n in numeros2:
    print(n)

lista_numeros = list(numeros) # pasa de tupla a lista