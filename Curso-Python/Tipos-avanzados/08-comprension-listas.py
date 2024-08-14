usuarios = [[4, "felipe"],
            [1,"clara", ],
            [2,"agustin"],
            [3,"leandro"]
            ]

"pasar de una lista de nombres e ids a solo nombes"

nombres_usuarios = []
for elemento in usuarios:
    nombres_usuarios.append(elemento[1])
print(nombres_usuarios)
print("")
#esto se puede hacer de una forma mas sencilla

#nombres = [expresion for item in items] -> ejemplo
nombres = [usuario[1] for usuario in usuarios]
ids = [usuario[0] for usuario in usuarios]
print(nombres)
print(ids)
print("")
#tranformamos la lista -> map

nombres_condicionados = [usuario for usuario in usuarios if usuario[0]>2]
#crea una lista (nombre e id) con los ids > 2
print(nombres_condicionados)
print(" ")
#filtamos la lista -> filter

nombres_condicionados2 = [usuario[1] for usuario in usuarios if usuario[0] > 2]
#crea una lista(nombre) con los ids > 2
print(nombres_condicionados2)
print("")
#filtramos y transformamos al mismo tiempo

nombres_usuarios = []
nombres_usuarios = list(map(lambda usuario: usuario[1], usuarios))
#transforma a solo nombres
print(nombres_usuarios)
print("")

menos_usuarios = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(menos_usuarios)