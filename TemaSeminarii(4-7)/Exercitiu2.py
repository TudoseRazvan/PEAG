import random
from math import sin

#Aceasta functie va genera o populatie aleatoare cu dim individui,
 #unde fiecare individ este un sir binar obtinut prin reprezentarea in baza 2 a unui fenotip (x, y).
  #Calitatea fiecarui individ (functia obiectiv) va fi memorata la sfarsitul fiecarei reprezentari cromozomiale.
def generate_population(dim):
    population = []
    # Generam o populatie aleatoare cu dim individui
    for _ in range(dim):
        # Generam un individ aleator reprezentat ca un sir binar
        individual = [random.randint(0, 1) for _ in range(2 * 12)]  # Pentru 12 biti pentru fiecare componenta a fenotipului (x, y)
        # Calculam functia obiectiv pentru fiecare individ si o memoram la sfarsitul listei
        fitness = calculate_fitness(individual)
        individual.append(fitness)
        population.append(individual)
    return population

def calculate_fitness(individual):
    # Extragem componente fenotipului (x, y) din sirul binar
    x = int("".join(map(str, individual[:12])), 2)
    y = int("".join(map(str, individual[12:])), 2)
    return y * (sin(x - 2) ** 2)

#Aceasta functie va realiza recombinarea intr-o populatie data folosind operatorul de incrucisare
 #multi-punct pentru 3 puncte de incrucisare.
  #Recombinarea consta in a lua doua perechi de parinti, a alege trei puncte aleatoare de taiere
def recombination(population, pc):
    recombinated_population = []
    for i in range(0, len(population), 2):
        # Alegem doua perechi de parinti
        parent1 = population[i]
        parent2 = population[i + 1]
        if random.random() < pc:
            # Alegem 3 puncte de taiere distincte
            points = sorted(random.sample(range(1, len(parent1) - 1), 3))
            child1 = parent1[:points[0]] + parent2[points[0]:points[1]] + parent1[points[1]:points[2]] + parent2[points[2]:]
            child2 = parent2[:points[0]] + parent1[points[0]:points[1]] + parent2[points[1]:points[2]] + parent1[points[2]:]
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
    print(ind[:-1], "Fitness:", ind[-1])

recombinated_population = recombination(population, pc)
print("\nPopulatia dupa recombinare:")
for ind in recombinated_population:
    print(ind[:-1], "Fitness:", ind[-1])
