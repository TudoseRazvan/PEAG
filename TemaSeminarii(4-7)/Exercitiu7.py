import random

#Aceasta functie va genera o populatie aleatoare cu dim individului, unde fiecare individ este o permutare de n elemente.
 #Calitatea fiecarui individ (functia obiectiv) va fi memorata la sfarsitul fiecarei reprezentari cromozomiale.
def generate_population(dim, n):
    population = []
    for _ in range(dim):
        individual = random.sample(range(1, n+1), n)  # Generăm o permutare aleatoare a elementelor de la 1 la n
        fitness = calculate_fitness(individual)
        individual.append(fitness)  #Memoram calitatea individului la sfarsitul listei
        population.append(individual)
    return population

#Aceasta functie calculeaza calitatea fiecarui individ, conform functiei obiectiv specificate.
def calculate_fitness(individual):
    fitness = 0
    n = len(individual)
    for i in range(n):
        for j in range(i+1, n):
            if individual[i] < individual[j] and individual[individual[i]-1] == j and individual[individual[j]-1] == i:
                fitness += 1
    return fitness


#Aceasta functie va realiza mutatia utilizand operatorul de mutatie prin amestec.
def mutation(population, pm):
    mutated_population = []
    for individual in population:
        if random.random() < pm:
            mutated_individual = individual[:-1]  #Eliminam calitatea individului pentru a face mutatia
            random.shuffle(mutated_individual)  #Amestecam aleator ordinea elementelor
            mutated_individual.append(calculate_fitness(mutated_individual))  # Recalculam calitatea individului
            mutated_population.append(mutated_individual)
        else:
            mutated_population.append(individual)
    return mutated_population

#Exemplu de folosire:
dim = 10
n = 5
pm = 0.1

population = generate_population(dim, n)
print("Populatia initiala:")
for ind in population:
    print(ind[:-1], "Fitness:", ind[-1])

mutated_population = mutation(population, pm)
print("\nPopulatia dupa mutatie:")
for ind in mutated_population:
    print(ind[:-1], "Fitness:", ind[-1])
