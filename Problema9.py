#Consideram spatiul solutiilor unei probleme format din vectori de dimensiune k, cu elemente numere intregi din multimea {-4,-3,-2,-1,1,2,3,4}  
#si cu proprietatea ca suma elementelor este pozitiva. Calitatea unui individ este data de suma modulelor elementelor sale (de exemplu, pentru k - 3 si x = [2,4,-3], 
#x este fezabil, pentru ca suma elementelor sale este 3 > 0, calitatea lui x este 9. 
#a) Scrieti o functie python pentru generarea aleatoare a unei populatii, pop, cu dimensiunea dim, calitatea fiecarui individ este memorata la sfarsitul reprezentarii sale 
#(se obtine o singura matrice, in care ultima coloana contine calitatile). 
#b) Scrieti o functie python care, pentru populatia generata pop si o probabilitate  de mutatie pm, obtine o populatie noua prin aplicarea 
#operatorului de mutatie resetare aleatoare. Daca un individ care a suferit macar o mutatie este nefezabil, el este inlocuit cu cel care l-a produs

import numpy as np

def generate_population(dim, k):
    population = np.random.choice([-4,-3,-2,-1,1,2,3,4], size=(dim, k))
    # Verificăm fiecare individ pentru a asigura că suma elementelor este pozitivă
    for i in range(dim):
        while np.sum(population[i]) <= 0:
            population[i] = np.random.choice([-4,-3,-2,-1,1,2,3,4], size=(k,))
    # Calculăm calitatea fiecărui individ și o adăugăm la finalul reprezentării sale
    quality = [np.sum(np.abs(individual)) for individual in population]
    population_with_quality = np.column_stack((population, quality))
    return population_with_quality

def mutation(population, pm):
    new_population = np.copy(population)
    dim, k_plus_1 = population.shape
    k = k_plus_1 - 1
    for i in range(dim):
        # Aplicăm mutația individualului cu o probabilitate pm
        if np.random.rand() < pm:
            mutated_individual = np.random.choice([-4,-3,-2,-1,1,2,3,4], size=(k,))
            # Dacă individul mutat este nefezabil, îl înlocuim cu cel original
            while np.sum(mutated_individual) <= 0:
                mutated_individual = np.random.choice([-4,-3,-2,-1,1,2,3,4], size=(k,))
            new_population[i, :-1] = mutated_individual
            # Recalculăm calitatea individului mutat și o actualizăm
            quality = np.sum(np.abs(mutated_individual))
            new_population[i, -1] = quality
    return new_population

# Exemplu de utilizare:
population = generate_population(10, 3)
print("Populația inițială:")
print(population)

population_after_mutation = mutation(population, 0.1)
print("\nPopulația după mutație:")
print(population_after_mutation)
