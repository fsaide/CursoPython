mascotas =  ["scarface", "pelusa", "negra", "daysi", "chispa"]

for mascota in mascotas:
    print(mascota)

espacio = """

"""
print(espacio)

for mascota in enumerate(mascotas): #enumera mascotas -> id, mascota
    print(mascota)
    print(mascota[0]) #imprime id
    print(mascota[1]) #imprime nombre
    print(" ")

print(espacio)

for indice, mascota in enumerate(mascotas): #en vez de tener una tupla mascota las separamos
    print(indice, mascota)