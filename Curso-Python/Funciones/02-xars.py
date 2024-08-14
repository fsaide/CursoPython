def suma(*numeros): #el * nos indica que tiene una cantidad x de parametros
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(5, 5)
suma(5, 5, 5)
suma(5, 5, 5, 5)