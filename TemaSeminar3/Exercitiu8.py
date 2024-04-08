import random

def generate_individual(k):
    while True:
        individual = random.choices([-4, -3, -2, -1, 1, 2, 3, 4], k=k)
        if sum(individual) > 0:
            return individual

def calculate_quality(individual):
    return sum(abs(x) for x in individual)

def generate_matrix(k):
    individuals = []

    for _ in range(10):
        individual = generate_individual(k)
        quality = calculate_quality(individual)
        individuals.append((individual, quality))

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

for individual, quality in individuals:
    print(f"Individ: {individual}, Calitate: {quality}")

min_quality = min(quality for individual, quality in individuals)

print(f"Calitatea minima: {min_quality}")
print("Indivizi cu calitatea minima:")
for individual, quality in individuals:
    if quality == min_quality:
        print(individual)
