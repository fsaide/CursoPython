punto = {"x": 1, "y": 2} #solamente acepta strings como key
print(punto) #imprime llave y valor
print(punto["x"]) #imprime el valor de x
print(punto["y"]) #imprime el valor de y
print(" ")

punto["z"] = 3 #agregue una 3ra key
print(punto)
print("")

if "g" in punto:
    print("encontre g en punto", punto["g"])


print(punto.get("x")) #imprime el valor de x
del punto["z"] #elimina la key z junto con su valor
print("")

for key in punto:
    print(key)

for valor in punto:
    print(punto[valor])

for tupla in punto.items():
    print(tupla)

for key, valor in punto.items():
    print(key, ":", valor)

usuarios = [
    {"id" : 1, "nombre" : "felipe"},
    {"id" : 2, "nombre" : "clara"},
    {"id" : 3, "nombre" : "leandro"}
]

for usuario in usuarios:
    print(usuario["nombre"])