import numpy as np

def generate_permutation():
    #Initializam o permutare aleatoare a primelor 6 numere naturale
    permutation = np.random.permutation(6)
    #Daca 1 se afla in prima jumatate, inversam permutarea
    while np.where(permutation == 1)[0][0] < 3:
        permutation = np.random.permutation(6)
    return permutation

def calculate_quality(permutation):
    #Calculam suma pozitiilor pe care apar valorile pare in permutare
    quality = sum(idx for idx, val in enumerate(permutation) if val % 2 == 0)
    return quality

def generate_population(n):
    #Initializam calitatea maxima cu cea mai mica valoare posibila
    max_quality = float('-inf')
    population = []
    for _ in range(n):
        permutation = generate_permutation()
        quality = calculate_quality(permutation)
        max_quality = max(max_quality, quality)
        population.append((permutation, quality))
    return population, max_quality

def print_population(population):
    for idx, (permutation, quality) in enumerate(population):
        print(f"Individul {idx + 1}: {permutation} - Calitate: {quality}")

n = int(input("Introduceti numarul de indivizi (n): "))

population, max_quality = generate_population(n)

print("Populatia generata:")
print_population(population)

print(f"\nValoarea maxima a calitatii: {max_quality}")
