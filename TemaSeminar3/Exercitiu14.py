import numpy as np
from itertools import permutations

def generate_permutation(k):
    # Generăm o permutare aleatoare a elementelor între 2 și k-1
    permutation = np.random.permutation(range(2, k))
    # Adăugăm prima și ultima poziție la permutare
    permutation = np.concatenate(([1], permutation, [k]))
    return permutation

def calculate_quality(permutation):
    quality = sum(1 for i in range(1, len(permutation)) if permutation[i-1] < i)
    return quality


def generate_population(k):
    population = []
    for _ in range(10):
        permutation = generate_permutation(k)
        quality = calculate_quality(permutation)
        population.append((permutation, quality))
    return population

def print_population(population):
    for idx, (permutation, quality) in enumerate(population, start=1):
        print(f"Individul {idx}: {permutation} - Calitate: {quality}")

# Citim valoarea lui k de la tastatură
k = int(input("Introduceți valoarea lui k: "))

# Generăm populația pentru valoarea lui k
population = generate_population(k)

# Afișăm populația generată
print("Indivizii generați:")
print_population(population)

# Afișăm valoarea maximă a calității
max_quality = max(quality for _, quality in population)
print(f"\nValoarea maximă a calității: {max_quality}")
