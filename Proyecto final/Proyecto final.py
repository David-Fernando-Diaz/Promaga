#reflexión en el suelo
import numpy as np
import matplotlib.pyplot as plt

class RayoReflejado:
    def __init__(self, xa, ya, xb, yb, sc, muestras):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.sc = sc
        self.muestras = muestras

    def calcular_punto_reflejado(self):
        numerador = self.xb * (self.sc - self.ya) - self.xa * (self.yb - self.sc)
        denominador = 2 * self.sc - self.ya - self.yb
        xc = numerador / denominador
        return xc, self.sc

    def graficar_rayos(self, xc):
        # Puntos en el plano
        plt.scatter([self.xa, xc, self.xb], [self.ya, self.sc, self.yb])
        plt.scatter([xc], [self.sc], label='punto reflejo')

        # Líneas de rayos
        plt.plot([self.xa, xc], [self.ya, self.sc], label='incidente')
        plt.plot([xc, self.xb], [self.sc, self.yb], label='reflejado')
        plt.plot([self.xa, self.xb], [self.sc, self.sc], label='suelo')

        # Etiquetas
        plt.annotate(' reflejo', [xc, self.sc])

        # Etiquetas
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Reflexión de rayos en plano')
        plt.grid()

        # Mostrar la gráfica
        plt.show()

def obtener_variables_usuario():
    xa = float(input("Ingrese la coordenada x del punto izquierdo (xa): "))
    ya = float(input("Ingrese la coordenada y del punto izquierdo (ya): "))
    xb = float(input("Ingrese la coordenada x del punto derecho (xb): "))
    yb = float(input("Ingrese la coordenada y del punto derecho (yb): "))
    sc = float(input("Ingrese la altura del suelo (sc): "))
    muestras = int(input("Ingrese el número de muestras en la gráfica (muestras): "))

    return xa, ya, xb, yb, sc, muestras

def main():
    xa, ya, xb, yb, sc, muestras = obtener_variables_usuario()

    rayo = RayoReflejado(xa, ya, xb, yb, sc, muestras)

    # Calcular punto reflejado
    punto_reflejado = rayo.calcular_punto_reflejado()
    print('Punto reflejado:', punto_reflejado)

    # Graficar rayos
    rayo.graficar_rayos(punto_reflejado[0])

if __name__ == "__main__":
    main()

"""Reflexion plano inclinado """

import numpy as np
import matplotlib.pyplot as plt

class RayoEnPlanoInclinado:
    def __init__(self, xa, ya, xb, yb, sa, sb, muestras=21):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.sa = sa
        self.sb = sb
        self.muestras = muestras

    def calcular_punto_reflejado(self):
        ms = (self.sb - self.sa) / (self.xb - self.xa)
        bs = self.sa - ms * self.xa

        numerador = bs * (self.xa + self.xb) - (self.xa * self.yb + self.xb * self.ya) + 2 * ms * self.xa * self.xb
        denominador = 2 * bs - (self.ya + self.yb) + ms * (self.xa + self.xb)

        xc = numerador / denominador
        sc = ms * xc + bs

        return xc, sc

    def visualizar_rayos(self, xc, sc):
        # Puntos en el plano
        plt.scatter([self.xa, xc, self.xb], [self.ya, sc, self.yb])
        plt.scatter([xc], [sc], label='punto reflejo')

        # Líneas de rayos
        plt.plot([self.xa, xc], [self.ya, sc], label='incidente')
        plt.plot([xc, self.xb], [sc, self.yb], label='reflejado')
        plt.plot([self.xa, self.xb], [self.sa, self.sb], label='suelo')

        # Etiquetas anotadas
        plt.annotate(' reflejo', [xc, sc])

        # Etiquetas
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Reflexión de rayos en plano inclinado')
        plt.grid()

        # Mostrar la gráfica
        plt.show()

def main():
    # Posición de antenas
    xa = 1  # Izquierda
    ya = 4
    xb = 11  # Derecha
    yb = 2

    # Altura del plano inclinado
    sa = 2
    sb = 1

    # Muestras en gráfica
    muestras = 21

    # Crear objeto de la clase RayoEnPlanoInclinado
    rayo = RayoEnPlanoInclinado(xa, ya, xb, yb, sa, sb, muestras)

    # Calcular punto reflejado
    punto_reflejado = rayo.calcular_punto_reflejado()
    print('Punto reflejado:', punto_reflejado)

    # Graficar rayos
    rayo.visualizar_rayos(punto_reflejado[0], punto_reflejado[1])

if __name__ == "__main__":
    main()

