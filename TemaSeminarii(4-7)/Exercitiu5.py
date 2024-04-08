import random

def generate_population(dim):
    population = []
    for _ in range(dim):
        individual = [random.randint(0, 1) for _ in range(7)]
        fitness = calculate_fitness(individual)
        individual.append(fitness)
        population.append(individual)
    return population

def calculate_fitness(individual):
    return sum(individual)

def recombination(population, pc):
    recombinated_population = []
    for i in range(0, len(population), 2):
        parent1 = population[i]
        parent2 = population[i + 1]
        if random.random() < pc:
            # Alegem 2 puncte de taiere distincte
            points = sorted(random.sample(range(1, len(parent1) - 1), 2))
            child1 = parent1[:points[0]] + parent2[points[0]:points[1]] + parent1[points[1]:]
            child2 = parent2[:points[0]] + parent1[points[0]:points[1]] + parent2[points[1]:]
        else:
            child1 = parent1
            child2 = parent2
        recombinated_population.append(child1)
        recombinated_population.append(child2)
    return recombinated_population

#Exemplu de folosire:
dim = 10
pc = 0.8

population = generate_population(dim)
print("Populatia initiala:")
for ind in population:
    print(ind[:-1], "Fitness:", ind[-1])

recombinated_population = recombination(population, pc)
print("\nPopulatia dupa recombinare:")
for ind in recombinated_population:
    print(ind[:-1], "Fitness:", ind[-1])
