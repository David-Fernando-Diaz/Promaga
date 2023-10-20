def fibonacci_generador(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

def numeros_pares_fibonacci_hasta_n(n):
    return (x for x in fibonacci_generador(n) if x % 2 == 0)

n = 100
numeros_pares = list(numeros_pares_fibonacci_hasta_n(n))

print("Serie de Fibonacci hasta", n, ":")
print(list(fibonacci_generador(n)))

print("\nNúmeros pares en la serie de Fibonacci hasta", n, ":")
print(numeros_pares)
