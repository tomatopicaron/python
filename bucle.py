def calcular_precio(horas):
    if horas == 1:
        precio = 900
    
    elif horas == 2:
        precio =1000
    
    elif horas == 4:
        precio = 1500
    
    else:
        precio = horas*400 #aqui calcule un precio justo para las cantidades no especificadsa
    
    return precio
horas = int(input("ingrese numero de horas. ejm: 2"))

precio = calcular_precio(horas)
print(f"precio por{horas} horas es: {precio}")

    
    

    
    
    
    
