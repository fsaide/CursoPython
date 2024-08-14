def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
       #return resultado  -> estaba mal escalado
    return resultado


print("detencion postFuncion") #marcamos breakpoint al costado del nro de linea
l = largo("Hola Mundo")
print(l)

#stepover pasa a la linea siguiente (f10)
#stepinto te ingresa dentro de la ejecucion de la funcion (f11)
#stepout te saca de la ejecucion de la funcion (f12)