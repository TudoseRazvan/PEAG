import random
from math import sin


#Definim functia obiectiv f(x)
def f(x):
    return (sin(x - 2)) ** 2


#a. Functia pentru generarea aleatoare a unei populatii
def generate_population(dim):
    population = []
    for _ in range(dim):
        #Genereaza un individ aleatoriu reprezentat ca un numar intreg aleatoriu intre 1 si 2500
        individual = random.randint(1, 2500)
        #Calculeaza calitatea (fitness-ul) fiecarui individ folosind functia obiectiv
        fitness = f(individual)
        #Adauga individul si calitatea lui la populatie
        population.append((individual, fitness))
    return population


#b. Functia pentru selectia de tip ruleta cu distributie de probabilitate FPS cu sigma-scalare
def roulette_wheel_selection(population):
    #Calculeaza suma fitness-urilor pentru intreaga populatie
    total_fitness = sum(fitness for _, fitness in population)

    #Calculeaza probabilitatea de selectie pentru fiecare individ
    probabilities = [fitness / total_fitness for _, fitness in population]

    #Selecteaza parinții folosind metoda ruletei
    parents = []
    for _ in range(len(population)):
        #Alege un numar aleatoriu între 0 si 1 pentru a selecta un individ
        random_number = random.random()
        cumulative_probability = 0
        for i, prob in enumerate(probabilities):
            cumulative_probability += prob
            if random_number <= cumulative_probability:
                parents.append(population[i])
                break

    return parents


#Exemplu de utilizare:
dimensiune_populatie = 50
populatie = generate_population(dimensiune_populatie)
print("Populatie generata aleatoriu:")
for individual, fitness in populatie:
    print(f"Individ: {individual}, Fitness: {fitness}")

parinti = roulette_wheel_selection(populatie)
print("\nParintii selectati prin selectia de tip ruleta:")
for individual, fitness in parinti:
    print(f"Individ: {individual}, Fitness: {fitness}")
