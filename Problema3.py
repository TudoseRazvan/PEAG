#Fie functia de maxim: f:{x=(x1,...,x10)/xi apartine lui [-1,1],
# x1 + ... x9 = 1 - x10} cu valori in R, f(x) = a1 x1 + ... + a10 x10 unde a = (a1, ... , a10)
# este un vector constant, data de intrare.
# a) Scrieti o functie python pentru generarea aleatoare a unei populatii, pop,
# cu dimensiunea dim, calitatea fiecarui individ este memorata intr-un vector calitate;
# b) Pentru o probabilitate de crossover data, pc, scrieti o functie de
# recombinare utilizand operatorul de recombinare aritmetica simpla,
# care pe baza populatiei pop obtine o noua populatie, copii.
# Populatia rezultata are tot dim indivizi.

import random

def generate_population(dim):
    population = []
    for _ in range(dim):
        # Generăm un individ aleator cu valorile xi între -1 și 1, iar x10 este calculat pentru a satisface condiția dată
        individual = [random.uniform(-1, 1) for _ in range(10)]
        individual[9] = 1 - sum(individual[:9])  # Calculăm x10 pentru a satisface condiția
        quality = evaluate_individual(individual)
        population.append((individual, quality))
    return population

def evaluate_individual(individual):
    # Definim vectorul constant a
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Calculăm valoarea funcției f pentru individul dat
    result = sum(a[i] * individual[i] for i in range(10))
    return result

def arithmetic_crossover(parent1, parent2):
    # Selecția unui punct de crossover aleator între 1 și 8 (poate fi schimbat în funcție de nevoi)
    crossover_point = random.randint(1, 8)
    # Realizarea crossover-ului aritmetic
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def recombination(population, pc):
    dim = len(population)
    new_population = []
    for i in range(dim):
        # Selecția aleatoare a doi părinți
        parent1, _ = random.choice(population)
        parent2, _ = random.choice(population)
        # Verificarea dacă crossover-ul trebuie aplicat
        if random.random() < pc:
            child1, child2 = arithmetic_crossover(parent1, parent2)
            # Evaluarea calității copiilor și adăugarea lor la noua populație
            quality1 = evaluate_individual(child1)
            quality2 = evaluate_individual(child2)
            new_population.append((child1, quality1))
            new_population.append((child2, quality2))
        else:
            # Adăugarea părinților nemodificați la noua populație
            new_population.append((parent1, evaluate_individual(parent1)))
            new_population.append((parent2, evaluate_individual(parent2)))
    return new_population

# Exemplu de utilizare:
population = generate_population(10)
print("Populația inițială:")
for individual, quality in population:
    print(f"Individual: {individual}, Quality: {quality}")

population_after_recombination = recombination(population, 0.8)
print("\nPopulația după recombinație:")
for individual, quality in population_after_recombination:
    print(f"Individual: {individual}, Quality: {quality}")
