
mayor = float('-inf')
menor = float('inf')

# Solicitamos al usuario diez números
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))
    
    # Actualizamos el número mayor si es necesario
    if numero > mayor:
        mayor = numero
    
    # Actualizamos el número menor si es necesario
    if numero < menor:
        menor = numero

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
