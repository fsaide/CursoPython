def esPalindromo(texto):
    textoaux = texto.lower()
    textoaux = textoaux.replace(" ", "")
    print(textoaux)
    for i in range(int(len(textoaux)/2)):
        f = len(textoaux) - 1 - i        
        inicio = textoaux[i]
        final = textoaux[f]
        if ( inicio != final):
            return False
    return True


es = esPalindromo("Amo la paloma")
if es:
    print("es palindromo")
else:
    print("no es palindromo")