def calcular_raiz_cuadrada_aproximada(numero, precision=0.00001):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    
    if numero == 0:
        return 0
    
    aproximacion = numero / 2  
    while abs(aproximacion ** 2 - numero) > precision:
        aproximacion = 0.5 * (aproximacion + numero / aproximacion)  
    
    return aproximacion

# Solicitar al usuario el número y la precisión deseada
numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))
precision = float(input("Ingrese la precisión deseada (por ejemplo, 0.00001): "))

raiz_aproximada = calcular_raiz_cuadrada_aproximada(numero, precision)
print(f"La raíz cuadrada aproximada de {numero} es aproximadamente {raiz_aproximada:.5f}")
