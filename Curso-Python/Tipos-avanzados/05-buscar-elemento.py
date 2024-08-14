mascotas =  ["scarface", "pelusa", "negra", "daysi", "chispa"]

mascotas.index("pelusa") #si el elemento existe en la lista devuelve indice
mascotas.index("No existe en la lista") #error

if "chispa" in mascotas:
    print(mascotas.index("chispa")) 
    #si chispa esta en la lista devuelve indice

print(mascotas.count("scarface")) #cuenta cuantas veces scarface en la lista
