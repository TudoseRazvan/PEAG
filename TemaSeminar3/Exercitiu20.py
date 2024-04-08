import numpy as np

def generate_individual():
    #Initializam un individ aleatoriu de dimensiune 6
    individual = np.random.choice([-2, -1, 0, 1, 2, 3, 4], size=6)
    #Verificam daca suma elementelor este mai mica decat 10
    while np.sum(individual) >= 10:
        individual = np.random.choice([-2, -1, 0, 1, 2, 3, 4], size=6)
    return individual

def calculate_quality(individual):
    #Calculam produsul valorilor absolute ale elementelor individului
    quality = np.prod(np.abs(individual))
    return quality

def generate_population():
    population = []
    for _ in range(10):
        individual = generate_individual()
        quality = calculate_quality(individual)
        population.append((individual, quality))
    return population

def print_population(population):
    #Sortam populatia in ordine inversa a calitatilor
    population_sorted = sorted(population, key=lambda x: x[1])
    for idx, (individual, quality) in enumerate(population_sorted, start=1):
        print(f"Individul {idx}: {individual} - Calitate: {quality}")

population = generate_population()

print("Indivizii generati in ordinea inversa a calitatilor:")
print_population(population)
