import math
import random

def f(x):
    return (math.sin(x - 2)) ** 2 - x * math.cos(x)

def hill_climbing(f, x_min, x_max, max_i):
    #Initializez solutia aleatoare
    solutie_curenta_x = random.uniform(x_min, x_max)
    valoare_curenta = f(solutie_curenta_x)

    for _ in range(max_i):
        #Generez o solutie vecina
        solutie_vecina_x = solutie_curenta_x + random.uniform(-0.1, 0.1)
        valoare_vecina = f(solutie_vecina_x)

        # Actualizez solutia curenta daca vecinul este mai bun
        if valoare_vecina > valoare_curenta:
            solutie_curenta_x = solutie_vecina_x
            valoare_curenta = valoare_vecina

    return solutie_curenta_x, valoare_curenta


# Specific intervalul pentru cautare si numarul maxim de iteratii
x_min = 1
x_max = 2500
max_i = 1000

# Aplicam algoritmul Hill-Climbing
max_x, max_value = hill_climbing(f, x_min, x_max, max_i)

print("Maximul functiei f este:", max_value)
print("Obtinut la x =", max_x)
