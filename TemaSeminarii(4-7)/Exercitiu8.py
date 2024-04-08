import random

#Aceasta functie genereaza o populatie aleatoare cu dim indivizi, unde fiecare individ este
 #o permutare a primelor n numere intregi pozitive. Calitatea fiecarui individ este calculata si memorata.
def generate_population(dim, n):
    population = []
    for _ in range(dim):
        individual = random.sample(range(1, n+1), n)
        fitness = calculate_fitness(individual)
        population.append((individual, fitness))
    return population

def calculate_fitness(individual):
    n = len(individual)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    fitness = n * ((n-1)//2) - conflicts
    return fitness

#Aceasta functie aplica procedura de inlocuire elitista, selectand cei mai buni indivizi
 #din cele doua populatii si formand astfel o noua populatie cu dim indivizi.
def elitist_replacement(pop1, pop2):
    combined_population = pop1 + pop2
    combined_population.sort(key=lambda x: x[1], reverse=True)  #Sortam populatia combinata dupa fitness in ordine descrescatoare
    new_population = combined_population[:len(pop1)]  #Selectam primii dim indivizi din populatia combinata
    return new_population

#Exemplu de folosire:
dim = 10
n = 8

pop1 = generate_population(dim, n)
pop2 = generate_population(dim, n)

#Aplicam procedura de inlocuire elitista
new_population = elitist_replacement(pop1, pop2)

print("Populatia rezultata:")
for ind, fit in new_population:
    print("Individ:", ind, "Fitness:", fit)
