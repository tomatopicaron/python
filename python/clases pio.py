suma = 0
for i in range (1,21):
    suma += i **2
print(suma)

a, b = 0, 1
while b <1000:
    print(b)
    a,b = b, a + b
    
suma = 0

for i in range(1,51):
    suma += i 
    print(suma)
    
numero = int(input("aqui va el numero"))
while numero >=1:
    print (numero) 
    numero -= 1
    
total = 0
while total < 100:
    number = int(input("ingrese un número: "))
    total += number
print(f"Total acumulado: {total}")


for i in range(10):
    if i == 5:
        break
    print(i)
    
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
    

puntaje = int(input("ingrese su puntaje"))

if puntaje > 100:
    print ("puntaje no valido")
    
if puntaje >= 90:
    print ("Exelente papáaaaa!")
    
if puntaje >= 75:
    print ("es bueno si")

if puntaje >= 50:
    print ("esta bien, pasas")

else: 
    print ("Perdiste, a estudiar papá!")