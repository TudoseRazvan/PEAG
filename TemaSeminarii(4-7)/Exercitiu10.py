import random

#Definim functia obiectiv f(x)
def f(x):
    return x ** 2

#a. Functia pentru generarea aleatoare a unei populatii
def generate_population(dim):
    population = []
    for _ in range(dim):
        # Generam un individ aleatoriu reprezentat ca un numar intreg aleatoriu intre 1 si 350
        individual = random.randint(1, 350)
        # Calculam calitatea (fitness-ul) fiecarui individ folosind functia obiectiv
        fitness = f(individual)
        # Adaugam individul si calitatea lui la populatie
        population.append((individual, fitness))
    return population

#b. Functia pentru aplicarea procedurii de tip GENITOR pentru obtinerea unei noi populatii
def genitor_selection(pop1, pop2):
    new_population = []
    for _ in range(len(pop1)):
        #Selecteaza aleatoriu doi indivizi din fiecare populatie
        parent1 = random.choice(pop1)
        parent2 = random.choice(pop2)
        #Inlocuieste primul individ din populatia rezultata cu parent1 si al doilea individ cu parent2
        new_population.append(parent1)
        new_population.append(parent2)
    return new_population

#Exemplu de utilizare:
dimensiune_populatie = 50

#Generam cele doua populatii
populatie1 = generate_population(dimensiune_populatie)
populatie2 = generate_population(dimensiune_populatie)

#Aplicam procedura de tip GENITOR pentru a obtine o noua populatie
noua_populatie = genitor_selection(populatie1, populatie2)

#Afiseaza noua populatie
print("Noua populatie obtinuta prin procedura de tip GENITOR:")
for individual, fitness in noua_populatie:
    print(f"Individ: {individual}, Fitness: {fitness}")
