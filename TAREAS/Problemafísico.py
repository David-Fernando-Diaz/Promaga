class Densidad:
    def __init__(self, masa, volumen):
        self.masa = masa
        self.volumen = volumen

    def calcular_densidad(self):
        if self.volumen == 0:
            return "El volumen no puede ser cero."
        else:
            return self.masa / self.volumen

# Solicitar al usuario la masa y el volumen
masa = float(input("Ingrese la masa en gramos: "))
volumen = float(input("Ingrese el volumen en litros: "))

# Crear un objeto Densidad
objeto_densidad = Densidad(masa, volumen)

# Calcular la densidad
densidad = objeto_densidad.calcular_densidad()

# Imprimir el resultado
print(f"La densidad es: {densidad} g/L")
