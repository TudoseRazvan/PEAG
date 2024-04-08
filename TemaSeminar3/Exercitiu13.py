import random
def generate_individual():
    return [random.uniform(-10, 10) for _ in range(7)]

def evaluate_individual(individual, coefficients):
    return sum(x * a for x, a in zip(individual, coefficients))

def generate_population(coefficients):
    population = []
    for _ in range(10):
        individual = generate_individual()
        population.append((individual, evaluate_individual(individual, coefficients)))
    return population

def find_max_quality(population):
    max_quality = max(quality for individual, quality in population)
    max_quality_individual = next(individual for individual, quality in population if quality == max_quality)
    return max_quality, max_quality_individual

coefficients = [float(input(f"Introduceti coeficientul a[{i+1}]: ")) for i in range(7)]

population = generate_population(coefficients)

max_quality, max_quality_individual = find_max_quality(population)
print("Calitatea maxima:", max_quality)
print("Individ cu calitatea maxima:", max_quality_individual)
