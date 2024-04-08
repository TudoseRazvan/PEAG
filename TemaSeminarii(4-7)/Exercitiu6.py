import random

#Aceasta functie va genera o populatie aleatoare cu dim individului, unde fiecare individ este un genotip
 #reprezentat ca un sir binar obtinut prin codificarea Gray a fenotipului.
def generate_population(dim):
    population = []
    for _ in range(dim):
        #Generam un individ aleatoriu ca un sir binar
        individual = [random.randint(0, 1) for _ in range(9)]  #Folosesc 9 biti pentru codificarea Gray a valorilor intre 1 si 350
        population.append(individual)
    return population

#Aceasta functie va realiza recombinarea intr-o populatie data folosind operatorul de incrucisare uni-punct.
 #Recombinarea consta in selectarea unui punct de taiere si interschimbarea sectiunilor dintre cei doi parinti.
def recombination(population, pc):
    recombinated_population = []
    for i in range(0, len(population), 2):
        parent1 = population[i]
        parent2 = population[i + 1]
        if random.random() < pc:
            # Alegem un punct de taiere
            point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]
        else:
            child1 = parent1
            child2 = parent2
        recombinated_population.append(child1)
        recombinated_population.append(child2)
    return recombinated_population

# Exemplu de folosire:
dim = 10
pc = 0.8

population = generate_population(dim)
print("Populatia initiala:")
for ind in population:
    print(ind)

recombinated_population = recombination(population, pc)
print("\nPopulatia dupa recombinare:")
for ind in recombinated_population:
    print(ind)
