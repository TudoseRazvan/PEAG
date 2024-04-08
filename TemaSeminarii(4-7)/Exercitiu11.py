import random
from math import sin, cos

#Definim functia obiectiv f(x)
def f(x):
    return (sin(x - 2)) ** 2 - x * (cos(2 * x))

#a. Functia pentru generarea aleatoare a unei populatii
def generate_population(dim):
    population = []
    for _ in range(dim):
        #Genereaza un individ aleatoriu reprezentat ca un numar intreg aleatoriu intre 1 si 500
        individual = random.randint(1, 500)
        #Calculeaza calitatea (fitness-ul) fiecarui individ folosind functia obiectiv
        fitness = f(individual)
        #Adauga individul si calitatea lui la populatie
        population.append((individual, fitness))
    return population

#b. Functia pentru selectia de tip turneu cu k indivizi
def tournament_selection(population, k):
    selected_parents = []
    for _ in range(len(population)):
        #Selecteaza aleatoriu k indivizi din populatie pentru a participa la turneu
        participants = random.sample(population, k)
        #Alege cel mai bun individ din participanti pe baza valorii de fitness
        winner = max(participants, key=lambda x: x[1])
        #Adauga castigatorul la lista de parinti selectati
        selected_parents.append(winner)
    return selected_parents

#Exemplu de utilizare:
dimensiune_populatie = 50
k = 5  #Numarul de indivizi din turneu

#Genereaza populatia initiala
populatie = generate_population(dimensiune_populatie)

#Aplica selectia de tip turneu pentru a obtine o populatie de parinti
parinti_selectati = tournament_selection(populatie, k)

#Afiseaza parintii selectati
print("Parintii selectati prin selectie de tip turneu:")
for parent, fitness in parinti_selectati:
    print(f"Individ: {parent}, Fitness: {fitness}")
