import json

def generador_productos_con_precio_superior(archivo, umbral):
    with open(archivo, 'r') as f:
        productos = json.load(f)
        for producto in productos:
            if producto['precio'] > umbral:
                yield producto

archivo = "productos.json"
umbral = 20.0  # Puedes ajustar este umbral según tus necesidades

for producto in generador_productos_con_precio_superior(archivo, umbral):
    print("Nombre:", producto["nombre"])
    print("Precio:", producto["precio"])
    print("Stock:", producto["stock"])
    print()
