
print("Bienvenido a mi calculadora")
print("Las operaciones son suma, resta, mul y div")
print("Para salir escriba \"salir\"")

resultado = ""

while True:
    if not resultado: #recordar que "" se toma como falso
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    operacion = input("Ingrese operacion: ")
    if operacion.lower() == "salir":
        break

    n2 = input("Ingrese siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if (operacion.lower() == "suma"):
        resultado += n2
    elif (operacion.lower() == "resta"):
        resultado -= n2
    elif (operacion.lower() == "mul"):
        resultado *= n2
    elif (operacion.lower() == "div"):
        resultado /= n2
    else:
        print("Operacion no valida")
        break
    print(f"Resultado = {resultado}")
