import numpy as np

def generate_population(n):
    population = []
    for _ in range(n):
        #Initializam un individ cu 10 elemente binare, toate fiind 0
        individual = np.zeros(10, dtype=int)
        #Setam primele 5 elemente ale individului la 1
        individual[:5] = 1
        #Amestecam elementele pentru a obtine 5 biti de 1 la intamplare
        np.random.shuffle(individual)
        #Calculam calitatea individului
        quality = np.sum(np.where(individual == 1)[0])
        population.append((individual, quality))
    return population

def print_population(population):
    for idx, (individual, quality) in enumerate(population):
        print(f"Individul {idx + 1}: {individual} - Calitate: {quality}")

n = int(input("Introduceți numărul de indivizi (n): "))

population = generate_population(n)
print_population(population)
