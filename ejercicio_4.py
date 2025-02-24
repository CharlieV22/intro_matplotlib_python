# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

fig = plt.figure()
fig.suptitle('Ejercicio 4', fontsize=16)

ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(x, y1, c= "brown", marker="o", label="y1 = x**2" )
ax1.set_facecolor("pink")
ax1.set_title("Graf 1")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid()
ax1.legend()

ax2.plot(x, y2, c= "blue", marker="<", label="y2 = x**3" )
ax2.set_facecolor("yellow")
ax2.set_title("Graf 1")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid()
ax2.legend()


ax3.plot(x, y3, c= "violet", marker=">", label="y3 = x**4" )
ax3.set_facecolor("blanchedalmond")
ax3.set_title("Graf 1")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.grid()
ax3.legend()

ax4.plot(x,y4, c= "orange", marker="^", label="y4 = np.sqrt(x)" )
ax4.set_facecolor("lime")
ax4.set_title("Graf 1")
ax4.set_xlabel("x")
ax4.set_ylabel("y")
ax4.grid()
ax4.legend()

plt.show()
print("terminamos")
