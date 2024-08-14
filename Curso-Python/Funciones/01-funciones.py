def hola(nombre, apellido = "N"): #def es la palabra reservada que sirve para definir una funcion
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Felipe", "Saide")
hola("Felipe") #tomara como apellido el valor N

#si por alguna casualidad se me olvida el orden en el que
#tengo que poner los parametros, se puede decir cual es cual

hola(apellido = "saide", nombre = "felipe") #funcionara de la misma manera 
                                            #aunque el orden este invertido