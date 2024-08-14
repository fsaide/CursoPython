numeros = [1, 2, 3]

#Horrible!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros #mejor!
print(primero, segundo, tercero)

primero, *otros = numeros #obtenemos el 1ero aparte y los demas en una lista
print(primero, otros)

numeros = list(range(1, 11))
primero, segundo, *otros = numeros
print(primero, segundo, otros)

primero, *otros, ultimo = numeros
print(primero, otros, ultimo)