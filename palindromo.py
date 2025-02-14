def es_palindromo(texto):
    texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpio == texto_limpio[::-1]

frase = input("Ingresa una palabra o frase: ")

yes_palindromo = es_palindromo(frase)

if yes_palindromo:
    print("Es un palíndromo!")
else:
    print("No es un palíndromo.")