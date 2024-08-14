mascotas = ["scarface", "negrita", "pelusa"]
print(mascotas)
print(mascotas[0]) #imprime scarface
mascotas[1] = "negra" #cambia negrita por negra
print(mascotas)
print(mascotas[0:2]) #imprime de la posicion 0 a 2
print(mascotas[::2]) #imprime solo las posiciones pares
print(mascotas[1::2]) #imprime solo las posiciones impares (ya que arrancamos desde 1)
print(mascotas[1:2:2]) #imprime posiciones impares desde 1 hasta 2

numeros = list(range(21))
print(numeros[::2]) #numeros pares
print(numeros[1::2]) #numeros impares