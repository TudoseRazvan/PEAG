import random
import math

def generate_population(dim):
    population = []
    for _ in range(dim):
        individual = [random.uniform(-1, 1), random.uniform(0, 0.2), random.uniform(0, 1), random.uniform(0, 5)]
        population.append(individual)
    return population

def mutation(population, pm):
    mutated_population = []
    t = 0.6  #pragul pentru mutatie
    sigma = t / 3  #deviatia standard derivata din pragul t
    for individual in population:
        if random.random() < pm:
            mutated_individual = []
            for gene in individual:
                mutated_gene = gene + random.gauss(0, sigma)
                #Daca individul mutat depaseste limitele, ajustam la limita
                mutated_gene = max(min(mutated_gene, 1), -1) if mutated_gene < 0 else min(max(mutated_gene, 0), 5)
                mutated_individual.append(mutated_gene)
            mutated_population.append(mutated_individual)
        else:
            mutated_population.append(individual)
    return mutated_population

#Exemplu de folosire:
dim = 10
pm = 0.1

population = generate_population(dim)
print("Populatia initiala:")
for ind in population:
    print(ind)

mutated_population = mutation(population, pm)
print("\nPopulatia dupa mutatie:")
for ind in mutated_population:
    print(ind)
