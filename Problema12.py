#Consideram spatiul solutiilor unei probleme format din permutarile de dimensiune k.
#Calitatea unui individ P (permutare de dimensiune k) este data  de numarul perechilor
#(i,i+1), pentru care P(i) = i+1 si P(i+1) = i;
#a) Scrieti o functie Python pentru generarea aleatoare a unei populatii pop, cu
# dimensiunea dim, calitatea fiecarui individ este memorata intr-un vector calitate
#b) Pentru o probabilitate de incrucisare data, pc, scrieti o functie de recombinare
#utilizand operatorul OCX, care pe baza populatiei pop obtine o noua populatie, copii.
#Populatia rezultata are tot dim indivizi.

import random

def generate_population(dim, k):
    population = []
    for _ in range(dim):
        # Generăm o permutare aleatoare de dimensiune k
        permutation = random.sample(range(1, k+1), k)
        quality = evaluate_permutation(permutation)
        population.append((permutation, quality))
    return population

def evaluate_permutation(permutation):
    # Numărăm perechile (i, i+1) pentru care P(i) = i+1 și P(i+1) = i
    count = 0
    for i in range(len(permutation) - 1):
        if permutation[i] == i + 1 and permutation[i+1] == i + 2:
            count += 1
    return count

def order_crossover(parent1, parent2):
    # Selectăm două puncte de crossover aleatorii
    point1 = random.randint(0, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)

    # Selecția secțiunii de crossover pentru fiecare părinte
    segment_parent1 = parent1[point1:point2 + 1]
    segment_parent2 = parent2[point1:point2 + 1]

    # Inițializarea copiilor cu secțiunea de crossover a părinților
    child1 = segment_parent1.copy()
    child2 = segment_parent2.copy()

    # Înlocuirea valorilor din părinții cu valorile corespunzătoare din celălalt părinte
    for i in range(len(parent1)):
        if parent2[i] not in segment_parent1:
            child1.append(parent2[i])
        if parent1[i] not in segment_parent2:
            child2.append(parent1[i])

    return child1, child2

def recombination(population, pc):
    dim = len(population)
    new_population = []
    for _ in range(dim // 2):
        # Selecția aleatoare a doi părinți
        parent1, _ = random.choice(population)
        parent2, _ = random.choice(population)
        # Verificarea dacă crossover-ul trebuie aplicat
        if random.random() < pc:
            child1, child2 = order_crossover(parent1, parent2)
            # Evaluarea calității copiilor și adăugarea lor la noua populație
            quality1 = evaluate_permutation(child1)
            quality2 = evaluate_permutation(child2)
            new_population.append((child1, quality1))
            new_population.append((child2, quality2))
        else:
            # Adăugarea părinților nemodificați la noua populație
            new_population.append((parent1, evaluate_permutation(parent1)))
            new_population.append((parent2, evaluate_permutation(parent2)))
    return new_population

# Exemplu de utilizare:
population = generate_population(10, 5)
print("Populația inițială:")
for individual, quality in population:
    print(f"Permutare: {individual}, Calitate: {quality}")

population_after_recombination = recombination(population, 0.8)
print("\nPopulația după recombinație:")
for individual, quality in population_after_recombination:
    print(f"Permutare: {individual}, Calitate: {quality}")
