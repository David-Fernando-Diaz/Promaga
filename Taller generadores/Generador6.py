def mas_de_cinco_letras(lista_de_palabras):
    for palabra in lista_de_palabras:
        if len(palabra) > 5:
            yield palabra

# Ejemplo de uso:
palabras = ["Mandarina", "Naranja", "piña", "fresa", "uva", "sandia", "Cereza","Melon","Manzana"]
generador = mas_de_cinco_letras(palabras)

for palabra in generador:
    print(palabra)
