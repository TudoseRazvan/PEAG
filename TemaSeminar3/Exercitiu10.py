import random

def calculate_f(individual, a):
    return sum(a[i] * individual[i] for i in range(len(individual)))

def generate_population(n):
    population = []
    for _ in range(n):
        individual = [random.choice([-1, 1]) for _ in range(10)]
        population.append(individual)
    return population

a = [random.uniform(-10, 10) for _ in range(10)]

while True:
    try:
        n = int(input("Introduceti numarul de indivizi in populatie (n): "))
        if n > 0:
            break
        else:
            print("Numarul trebuie sa fie un numar intreg pozitiv.")
    except ValueError:
        print("Introduceti un numar intreg valid pentru n.")

population = generate_population(n)

max_f = max(calculate_f(individual, a) for individual in population)
print("Calitatea maxima:", max_f)
