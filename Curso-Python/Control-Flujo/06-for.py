buscar = 3

for numero in range(5): #range es un iterable, al igual que 
    print(numero)       #listas,tuplas o incluso los strings
    if (numero == buscar):
        print("Encontrado: ", numero)
        break
else: #en este caso sirve para saber si terminamos o no antes las iteraciones
    print("Numero no encontrado: ", numero)

for char in "Ultimate Python":
    print(char)

