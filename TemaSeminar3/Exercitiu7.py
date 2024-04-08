import random
import numpy as np

def generate_individual():
    individual = random.choices([1, 2, 3, 4], k=8)
    individual[4] = random.choice([1, 3])  # Asiguram ca valoarea de pe pozitia a 5-a este impara
    return individual

def calculate_quality(individual):
    return np.prod(individual)

def generate_matrix(n):
    individuals = []

    for _ in range(n):
        individual = generate_individual()
        quality = calculate_quality(individual)
        individuals.append((individual, quality))

    return individuals

while True:
    try:
        n = int(input("Introduceti numarul de indivizi (numar intreg pozitiv): "))
        if n > 0:
            break
        else:
            print("Numarul trebuie sa fie un numar intreg pozitiv.")
    except ValueError:
        print("Introduceti un numar intreg valid.")

individuals = generate_matrix(n)

for individual, quality in individuals:
    print(f"Individ: {individual}, Calitate: {quality}")

min_quality = min(quality for individual, quality in individuals)

print(f"Calitatea minima: {min_quality}")
print("Indivizi cu calitatea minima:")
for individual, quality in individuals:
    if quality == min_quality:
        print(individual)
