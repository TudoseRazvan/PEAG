import random

def generate_population(dim, n):
    population = []
    for _ in range(dim):
        individual = random.sample(range(1, n + 1), n)
        #Calculeaza functia obiectiv pentru fiecare individ si o memoreaza la sfarsitul listei
        fitness = calculate_fitness(individual)
        individual.append(fitness)
        population.append(individual)
    return population

def calculate_fitness(individual):
    #Implementeaza functia obiectiv: numara perechile (i, j) care satisfac conditiile
    count = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if i < j and individual[i] == j+1 and individual[j] == i+1:
                count += 1
    return count

def mutation(population, pm):
    mutated_population = []
    for individual in population:
        if random.random() < pm:
            #Alege doua pozitii aleatorii
            pos1, pos2 = sorted(random.sample(range(len(individual) - 1), 2))
            #Inverseaza segmentul dintre aceste pozitii
            individual[pos1:pos2+1] = reversed(individual[pos1:pos2+1])
        mutated_population.append(individual)
    return mutated_population

#Exemplu de folosire:
dim = 10
n = 5
pm = 0.1

population = generate_population(dim, n)
print("Populatia inițiala:")
for ind in population:
    print(ind[:-1], "Fitness:", ind[-1])

mutated_population = mutation(population, pm)
print("\nPopulatia dupa mutatie:")
for ind in mutated_population:
    print(ind[:-1], "Fitness:", ind[-1])
