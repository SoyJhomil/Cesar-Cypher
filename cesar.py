mensaje = input("Ingresa el mensaje a codificar: ") #Aqui se lee el mensaje para codificar
posiciones = int(input("Posiciones a mover: ")) # Aqui se lee la cantidad de posiciones que va a mover el algoritmo Cesar

def codific(mensaje, posiciones):
    alfabeto = "0123456789abcdefghijklmnopqrstuvwxyz" #Nuestro abc en minuscula + los numeros
    alfabeto_mayusculas = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Nuestro abc en mayuscula + los numeros
    longitud_alfabeto = len(alfabeto) #Aqui se determina la longitud del alfabeto
    codificado = "" #Esta variable guardara el resultado del mensaje codigicado
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)
        # Suponemos que es minúscula, así que esto comienza en 97(a) en el codigo ASCII y se usará el alfabeto en minúsculas
        alfabeto_a_usar = alfabeto
        limite = 97  # Pero si es mayúscula o un numero, comienza en 48(0)
        if letra.isupper():
            limite = 48
            alfabeto_a_usar = alfabeto_mayusculas

        # Movemos la letra x cantidad de posiciones
        posicion = (valor_letra - limite + posiciones) % longitud_alfabeto

        # Convertimos el entero resultante a letra y lo concatenamos
        codificado += alfabeto_a_usar[posicion]
    return codificado

codificado = codific(mensaje, posiciones) #Resultado del algoritmo que se va a guardar en la variable codificado
print ("Su mensaje codificado es: ", codificado) #Imprime el mensaje codificado
