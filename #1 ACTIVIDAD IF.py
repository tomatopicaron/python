def f(x):
    # Definir aquí la función cuya raíz se desea encontrar
    return x**3 - 2*x - 5  # Ejemplo: f(x) = x^3 - 2x - 5

def bolzano(a, b, E):
    if f(a) * f(b) > 0:
        print("Error: La función tiene el mismo signo en los extremos.")
        return None

    while (b - a) / 2 > E:
        c = (a + b) / 2  # Punto medio
        if f(c) == 0:
            return c  # Si c es la raíz exacta
        elif f(a) * f(c) < 0:
            b = c  # La raíz está en el intervalo [a, c]
        else:
            a = c  # La raíz está en el intervalo [c, b]

    c = (a + b) / 2  # Valor aproximado de la raíz
    return c

# Entradas del usuario
a = float(input("Ingrese el extremo inferior del intervalo (a): "))
b = float(input("Ingrese el extremo superior del intervalo (b): "))
E = float(input("Ingrese el error máximo permitido (E): "))

# Calcular y mostrar la raíz
raiz = bolzano(a, b, E)
if raiz is not None:
    print(f"El valor C que está a menos de {E} del valor c es: {raiz:.5f}")