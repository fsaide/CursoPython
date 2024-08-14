saludo = " Hola Global! "

def saludar():
    global saludo #utiliza una variable local, NO RECOMENDADO!
    print(saludo)

def saludarChanchito():
    saludo = " Hola chanchito"
    print(saludo)

#las variables creadas dentros de las funciones, solo tienen alcance
#dentro de la misma funcion, es decir, la variable saludo de saludar no es 
#la misma que la de saludarchanchito y en el main no existe la variable saludar

saludar()
saludarChanchito()
saludar()