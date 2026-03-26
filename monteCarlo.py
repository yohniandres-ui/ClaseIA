import random

def estimar_pi(n_puntos):
    dentro_circulo = 0

    for _ in range(n_puntos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            dentro_circulo += 1

    pi_estimado = 4 * dentro_circulo / n_puntos
    return pi_estimado

n = 10000
resultado = estimar_pi(n)

print("Estimación de π:", resultado)