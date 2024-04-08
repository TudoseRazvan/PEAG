import random

def generate_individual(k):
    return [random.randint(0, 1) for _ in range(k)]

def calculate_quality(individual):
    quality = 0
    for i in range(len(individual) - 1):
        if individual[i] == individual[i + 1]:
            quality += 1
    return quality

def generate_matrix(k):
    individuals = []

    for _ in range(10):
        individual = generate_individual(k)
        quality = calculate_quality(individual)
        individuals.append((individual, quality))

    individuals.sort(key=lambda x: x[1])  #Sortare dupa calitate
    return individuals

while True:
    try:
        k = int(input("Introduceti dimensiunea k a individului (numar intreg pozitiv): "))
        if k > 0:
            break
        else:
            print("Dimensiunea k trebuie sa fie un numar intreg pozitiv.")
    except ValueError:
        print("Introduceti un numar intreg valid pentru dimensiunea k.")

individuals = generate_matrix(k)

print("Indivizi in ordinea crescatoare a calitatilor:")
for individual, quality in individuals:
    print(f"Individ: {individual}, Calitate: {quality}")
