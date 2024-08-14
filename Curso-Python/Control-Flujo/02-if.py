edad = 87
if (edad > 17):
    print("Puede ver la pelicula")
    if (edad > 55):
        print("Descuento aplicado")
elif (edad>15):
    print("Acceso limitado")
else:
    print("No puede ver la pelicula")

print("Programa finalizado")

#Tener en cuenta que las condiciones se ejecutaran
#en el orden en el que se escriben
# 1.(edad > 17) 2.(edad>15) 3.(else)