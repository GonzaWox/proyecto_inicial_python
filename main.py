import csv
import random
import interfaz


if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    juego_nuevo = True
    while juego_nuevo is True:
        juego = ""
        max_cantidad_intentos = 7
        intentos = 0
        letras_usadas = []
        lista_palabras_secretas = []
        es_ganador = False

        def leer_palabra_secreta(csvfilename):
            csvfilename = open("palabras.csv")
            lista_palabras = list(csv.DictReader(csvfilename))
            
            for palabra in lista_palabras:
                lista_palabras_secretas.append(palabra["palabras"])
                print(lista_palabras_secretas)

            palabra_secreta = random.SystemRandom().choice(lista_palabras_secretas)
            print(palabra_secreta)
            return palabra_secreta


        def pedir_letra(letras_usadas):
            valido = False
            while valido is False:
                letra_usuario = str(input("Ingrese una letra:  "))
                if letra_usuario.isalpha():
                    letra = letra_usuario[0].lower()
                    valido = True
                else:
                    print(f"ERROR!! Ingrese unicamente una letra")
                    valido = False
            return letra


        def verificar_letra(letra, palabra_secreta):
            lista_palabra_secreta = list(palabra_secreta)
            if letra in lista_palabra_secreta:
                print(f"La letra ingresada está en la palabra ")
                return True
            else:
                print(f"La letra ingresada no está en la palabra")
                return False
        

        def validar_palabra(letras_usadas, palabra_secreta):
            contador = 0
            cantidad_letras = len(palabra_secreta)
            letras_palabra = list(palabra_secreta)
            for letra in letras_usadas:
                for letra_palabra in letras_palabra:
                    if letra == letra_palabra:
                        contador = contador + 1
                    
            if contador == cantidad_letras:
                return True
            else:
                print(f"Aun no se adivino la palabra")
                return False

        palabra_secreta = leer_palabra_secreta('palabras.csv')
        
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
        
        while intentos < max_cantidad_intentos and es_ganador == False:
            # Pedir una nueva letra
            letra = pedir_letra(letras_usadas)
            letras_usadas.append(letra)

            # Verificar si la letra es parte de la palabra secreta        
            if verificar_letra(letra, palabra_secreta) == False:
                # En caso de no estar la letra ingresada en la palabra
                # a adivinar incremento en 1 la variable intentos.
                intentos += 1
            
            # Dibujar la interfaz
            interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

            # Validar si la palabra secreta se ha adivinado
            if validar_palabra(letras_usadas, palabra_secreta) == True:
                es_ganador = True
                break

        if es_ganador is True:
            print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
        else:
            print('\n¡Ahorcado!')
            print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')

        while juego != "SI" and juego != "NO":

            juego = str(input("Quiere volver a jugar? [ SI / NO ] :"))
            if juego.isalpha():
                juego = juego.upper()
                if juego == "SI" or juego == "NO":
                    if juego == "SI":
                        juego_nuevo = True
                    if juego == "NO":
                        print("Gracias por jugar!")
                        juego_nuevo = False
                else:
                    print("ERROR!! Ingrese respuesta valida [ SI / NO ]")
            else:
                print("ERROR!! Ingrese respuesta valida [ SI / NO ]")
            