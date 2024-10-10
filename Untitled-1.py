def adivina_numero():
    print("Piensa un número entre 1 y 1000")
    minimo = 1
    maximo = 1000
    intentos = 0

    while intentos < 10:
        intentos += 1
        numero = (minimo + maximo) // 2
        print(f"¿El número es {numero}?")

        respuesta = input("Responde con <, > o =: ")

        if respuesta == "=":
            print(f"¡Adiviné! El número es {numero}.")
            print(f"Intentos necesarios: {intentos}")
            return

        elif respuesta == "<":
            if numero == minimo:
                print("estas haciendo trampa. ¿no?")
                return
            maximo = numero - 1

        elif respuesta == ">":
            if numero == maximo:
                print("¡Tramposo! No puedes decir que es mayor que el máximo.")
                return
            minimo = numero + 1

        else:
            print("Respuesta inválida. Por favor, responde con <, > o =.")

    print("No pude adivinar el número en 10 intentos.")

adivina_numero()