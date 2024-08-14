numeros = [2, 7, 4, 1, 45, 74, 22]

numeros.sort() #ordena la lista
print(numeros)
print(" ")

numeros.sort(reverse=True) #ordena la lista de mayor a menor
print(numeros)
print(" ")

numeros = [2, 7, 4, 1, 45, 74, 22]
numeros2 = sorted(numeros) #devuelve nueva lista, no afecta a la principal
print(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)
print(" ")

usuarios = [[4, "felipe"], [1,"clara", ], [2,"agustin"], [3,"leandro"]]
print(usuarios)
usuarios.sort() #ordena en base a la cordenada 0 de la tupla
print(usuarios)
print(" ")

def ordena(elemento):
    return elemento[1]
#les pasamos las tuplas de la lista y devuelve la de la posicion 1
#siendo en este caso los nombres

usuarios.sort(key=ordena) #ordena en base a los nombres
print(usuarios)
print(" ")

#a ordena no le pasamos como parametro elemento por que de eso se 
#se encarga la funcion sort por dentro, pasandole key

#otra forma de hacer lo mismo es de la siguiente manera:
usuarios = [[4, "felipe"], [1,"clara", ], [2,"agustin"], [3,"leandro"]]
usuarios.sort(key=lambda el:el[1])
print(usuarios)
