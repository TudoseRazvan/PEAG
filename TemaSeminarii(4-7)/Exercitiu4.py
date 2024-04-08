import random
from math import sin, cos

#Aceasta functie va genera o populatie aleatoare cu dim individui,
 #unde fiecare individ este un vector genotip x. Valorile x vor fi alese aleatoriu din intervalele specificate.
  #Functia merit va fi calculata pentru fiecare individ si va fi atasata acestuia.
def generate_population(dim):
    population = []
    for _ in range(dim):
        individual = [random.uniform(-1, 1), random.uniform(0, 1), random.uniform(-2, 1)]
        merit = calculate_merit(individual)
        individual.append(merit)
        population.append(individual)
    return population

def calculate_merit(individual):
    x1, x2, x3 = individual
    merit = 1 + sin(2*x1 - x3) + cos(x2)
    return merit

#Aceasta functie va realiza recombinarea utilizand operatorul de recombinare aritmetica totala.
 #Recombinarea consta in calcularea mediei ponderate intre perechile de parinti
  #pentru a obtine noii indivizi.
def recombination(population, pc):
    recombinated_population = []
    for i in range(0, len(population), 2):
        parent1 = population[i]
        parent2 = population[i + 1]
        if random.random() < pc:
            child1 = [(p1 + p2) / 2 for p1, p2 in zip(parent1[:-1], parent2[:-1])]  #Recombinare aritmetica
            child1.append((parent1[-1] + parent2[-1]) / 2)  #Calculeaza meritul pentru noul individ
            child2 = [(p1 + p2) / 2 for p1, p2 in zip(parent2[:-1], parent1[:-1])]
            child2.append((parent1[-1] + parent2[-1]) / 2)
        else:
            child1 = parent1[:]
            child2 = parent2[:]
        recombinated_population.append(child1)
        recombinated_population.append(child2)
    return recombinated_population

#Exemplu de folosire:
dim = 10
pc = 0.8

population = generate_population(dim)
print("Populația initiala:")
for ind in population:
    print(ind)

recombinated_population = recombination(population, pc)
print("\nPopulatia dupa recombinare:")
for ind in recombinated_population:
    print(ind)
