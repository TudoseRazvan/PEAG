import numpy as np


def generate_population(k, num_individuals):
    population = []
    for _ in range(num_individuals):
        #Generam un individ cu k elemente intregi aleatoare din multimea specificata
        individual = np.random.choice([1, 2, 3, 4, 5, 6], size=k, replace=True)
        #Adaugam o valoare para la sfarsitul individului
        individual = np.append(individual,
                               np.random.choice([2, 4, 6]))
        #Calculam calitatea individului ca produsul elementelor sale
        quality = np.prod(individual)
        population.append((individual, quality))

    #Sortam populatia in functie de calitatea indivizilor
    population.sort(key=lambda x: x[1])
    return population


def print_population(population):
    for idx, (individual, quality) in enumerate(population):
        print(f"Individul {idx + 1}: {individual} - Calitate: {quality}")


k = int(input("Introduceți dimensiunea individului (k): "))

population = generate_population(k, 10)

print_population(population)
