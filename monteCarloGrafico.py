import random
import matplotlib.pyplot as plt

def estimar_pi_visual(n_puntos):
    dentro_x = []
    dentro_y = []
    fuera_x = []
    fuera_y = []
    
    dentro_circulo = 0

    for _ in range(n_puntos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            dentro_circulo += 1
            dentro_x.append(x)
            dentro_y.append(y)
        else:
            fuera_x.append(x)
            fuera_y.append(y)

    pi_estimado = 4 * dentro_circulo / n_puntos

    plt.scatter(dentro_x, dentro_y, s=1)
    plt.scatter(fuera_x, fuera_y, s=1)
    plt.title(f"Estimación de π = {pi_estimado}")
    plt.show()

    return pi_estimado

estimar_pi_visual(100000)