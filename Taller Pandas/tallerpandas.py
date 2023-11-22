

"""Taller: Manejo de librerıas 1"""
"""
Objetivo del taller

El objetivo de este taller es poner a prueba y mejorar las habilidades de programacion en Python de los estudiantes de Programacion del programa de Fısica,
centrandose en el manejo de las bibliotecas Pandas y Numpy, la comprension
de generadores, el uso de funciones, clases, manejo de excepciones, *args y
**kwargs, y la aplicacion de conceptos de algebra lineal a la fısica.
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Ejercicio 1: Analisis de Datos con Pandas y Numpy

# 1. Importa las bibliotecas Pandas y Numpy.

# 2. Lee un archivo CSV llamado "datos fisica.csv" que contiene datos experimentales.

# 3. Define una funcion llamada analizar datos que acepte *args con una
# lista de nombres de columnas y **kwargs con operaciones (por ejemplo,
# media, mediana, desviacion). Maneja adecuadamente los errores que
# puedan surgir!

# 4. Utiliza Pandas y Numpy para realizar las operaciones especificadas en los
# datos seleccionados.
################################################################

# 1. Importar las bibliotecas Pandas y Numpy.
# import pandas as pd
# import numpy as np

# # # tabla1=pd.read_csv("estudiante.csv")
# # # tabla=tabla1.head(6)
# # # print(tabla)


# # 2. Leer un archivo CSV llamado "datos fisica.csv" que contiene datos experimentales.
# def read_csv_file(file_name):
#     try:
#         data = pd.read_csv(file_name)
#         return data
#     except FileNotFoundError:
#         print("No se encontró el archivo especificado.")
#         return None

# file_name = "datos fisica.csv"
# data = read_csv_file(file_name)

# # 3. Definir una función llamada analizar_datos que acepte *args con una lista de nombres de columnas y **kwargs con operaciones.
# def analizar_datos(data, *args, **kwargs):
#     try:
#         result = {}
#         for column_name in args:
#             if column_name in data.columns:
#                 result[column_name] = {}
#                 for operation in kwargs.keys():
#                     if operation == 'media':
#                         result[column_name]['media'] = np.mean(data[column_name])
#                     elif operation == 'mediana':
#                         result[column_name]['mediana'] = np.median(data[column_name])
#                     elif operation == 'desviacion':
#                         result[column_name]['desviacion'] = np.std(data[column_name])
#                     else:
#                         print(f"Operación no válida: {operation}")
#             else:
#                 print(f"No se encontró la columna: {column_name}")

#         return result
#     except Exception as e:
#         print("Error al analizar los datos:", str(e))
#         return None

# # 4. Utilizar Pandas y Numpy para realizar las operaciones especificadas en los datos seleccionados.
# columnas = ["columna1", "columna2"]
# operaciones = {"media": True, "mediana": True, "desviacion": True}

# resultado = analizar_datos(data, *columnas, **operaciones)

# # Imprimir el resultado
# for columna, valores in resultado.items():
#     print(f"Resultados para la columna '{columna}':")
#     for operacion, valor in valores.items():
#         print(f"{operacion}: {valor}")

# ```

# Este código importa las bibliotecas Pandas y Numpy, lee un archivo CSV llamado "datos fisica.csv" utilizando la función `read_csv_file`, define la función `analizar_datos` para realizar las operaciones especificadas en los datos seleccionados y utiliza Pandas y Numpy para realizar estas operaciones. Finalmente, imprime los resultados obtenidos.

# Recuerda reemplazar "datos fisica.csv" por el nombre y ubicación correcta de tu archivo CSV.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Ejercicio 2: Comprension de Generadores y Funciones con Serie de Taylor

# 1. Define una funcion generadora llamada generador taylor que genere los
# terminos de una serie de Taylor para una funcion matematica dada.

# 2. Permite que el usuario ingrese la funcion, el valor de x, la cantidad de
# terminos y otros parametros mediante **kwargs.

# 3. Utiliza esta funcion generadora para calcular y mostrar una estimacion
# basada en la serie de Taylor de la funcion especificada.

################################################################################

# def generar_serie_taylor(funcion, x_valor, num_terminos, **kwargs):
#     suma = 0.0
#     termino = 1.0

#     for n in range(num_terminos):
#         suma += termino
#         termino *= (funcion(x_valor, **kwargs) * (x_valor - 0) / (n + 1))

#     return suma

# # Ejemplo de uso:
# if __name__ == "__main":
#     def funcion_ejemplo(x, **kwargs):
#         return x ** 2  # Puedes cambiar esta función a la que desees

#     x_valor = float(input("Ingrese el valor de 'x': "))
#     num_terminos = int(input("Ingrese la cantidad de términos en la serie de Taylor: "))

#     estimacion = generar_serie_taylor(funcion_ejemplo, x_valor, num_terminos)

#     print(f"Estimación basada en la serie de Taylor: {estimacion}")





""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Ejercicio 3: Clases, Objetos, Excepciones y *argsy **kwargs

# 1. Crea una clase llamada Particula que tenga atributos como la masa, la
# carga y la posicion en tres dimensiones (x, y, z).

# 2. Define un metodo en la clase Particula que calcule la energıa cinetica de
# la partıcula utilizando la formula E =0.5*m*v*v.# , donde m es la masa y v es
# la velocidad de la partıcula.

# 3. Implementa manejo de excepciones para asegurarte de que la masa sea un
# numero positivo y permite que otros atributos sean configurados utilizando
# **kwargs.

# 4. Crea un objeto de la clase Particula con valores arbitrarios y calcula su
# energıa cinetica. Maneja las excepciones apropiadamente.

###########################################################################


# class Particula:
#     def __init__(self, masa, carga, x=0, y=0, z=0, **kwargs):
#         if masa <= 0:
#             raise ValueError("La masa debe ser un número positivo")
            
#         self.masa = masa
#         self.carga = carga
#         self.posicion = (x, y, z)
        
#         for key, value in kwargs.items():
#             setattr(self, key, value)
            
#     def calcular_energia_cinetica(self, velocidad):
#         try:
#             energia_cinetica = 0.5 * self.masa * velocidad**2
#             return energia_cinetica
#         except AttributeError:
#             print("No se puede calcular la energía cinética sin una velocidad definida")



# try:
#     particula = Particula(masa=2, carga=1, x=3, y=4, z=5, velocidad=10)
#     energia_cinetica = particula.calcular_energia_cinetica(particula.velocidad)
#     print("La energía cinética de la partícula es:", energia_cinetica)
# except ValueError as e:
#     print("Error:", e)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ejercicio 4: Algebra Lineal con Pandas y Numpy  (N × N).

# 1. Define una funcion llamada resolver sistema lineal que acepte una
# matriz A y un vector B como argumentos, junto con **kwargs que permitan configurar el metodo de resolucion (por ejemplo, ’eliminacion gaussiana’,
# ’descomposicion LU’).

# 2. Utiliza Numpy para resolver el sistema de ecuaciones Ax = B segun el
# metodo especificado.

# 3. Verifica la solucion calculando Ax y comparandola con B para comprobar
# si x es la solucion correcta.

# El taller es para realizar individual o en parejas y explicar la solucion de uno
# u varios puntos a eleccion del docente el dıa viernes 20 de octubre.

######################################################################

import numpy as np
import pandas as pd

def resolver_sistema_lineal(A, B, metodo='eliminacion_gaussiana', **kwargs):
    if metodo == 'eliminacion_gaussiana':
        x = np.linalg.solve(A, B)
    elif metodo == 'descomposicion_LU':
        P, L, U = scipy.linalg.lu(A)
        y = np.linalg.solve(L, B)
        x = np.linalg.solve(U, y)
    else:
        raise ValueError("Método no soportado")

    return x

# Ejemplo de uso
A = np.array([[2, 1], [5, 3]])
B = np.array([1, 2])
x = resolver_sistema_lineal(A, B, metodo='eliminacion_gaussiana')

# Verificación
resultado = np.dot(A, x)
print("Resultado del sistema Ax:", resultado)
print("Vector B:", B)

# Comparar el resultado con B
if np.allclose(resultado, B):
    print("La solución es correcta.")
else:
    print("La solución no es correcta.")


