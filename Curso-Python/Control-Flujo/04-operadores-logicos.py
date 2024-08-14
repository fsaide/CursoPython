# and, or, not
gas = True
encendido = True

if gas and encendido: #11
    print("Puedes avanzar")
elif not gas and not encendido: #00
    print("Falta gas y el auto no esta encendido")
elif not gas and encendido: #01
    print("El auto esta encendido pero falta gas")
elif gas and not encendido: #10
    print("El auto tiene gas pero falta encenderlo")