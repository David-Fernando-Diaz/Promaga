def kilogramos_a_libras(kilogramos):
    return kilogramos * 2.20462

def obtener_kilogramos_validos():
    while True:
        try:
            kilogramos = float(input("Ingrese la cantidad en kilogramos: "))
            if kilogramos < 0:
                print("Por favor, ingrese un valor positivo en kilogramos.")
            else:
                return kilogramos
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

# Solicitar los kilogramos al usuario
kilogramos = obtener_kilogramos_validos()

libras = kilogramos_a_libras(kilogramos)
print(f"{kilogramos} kilogramos son aproximadamente {libras} libras.")
