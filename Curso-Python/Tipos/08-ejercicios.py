n1 = input("Ingrese 1er valor: ")
n2 = input("Ingrese 2do valor: ")
# los datos ingresados son valores de tipo STRING cuidado con eso, hay que
# pasarlo a tipo de dato INTEGER

n1 = int(n1)
n2 = int(n2)
#con esto ya lo estariamos transformando a tipo INTEGER

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f""" Para los valores de n1 y n2
Los resultados de la suma de {n1} y {n2} son {suma}.
Los resultados de la resta de {n1} y {n2} son {resta}.
Los resultados de la multiplicacion de {n1} y {n2} son {multi}.
Los resultados de la division de {n1} y {n2} son {div}."""

print(mensaje)