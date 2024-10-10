#tablero
def es_perfecto(n):
    if n < 1:
        return False
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

# Prueba el código
n = int(input("Ingrese un número entero: "))
if es_perfecto(n):
    print(f"El número {n} es perfecto.")
else:
    print(f"El número {n} no es perfecto.")