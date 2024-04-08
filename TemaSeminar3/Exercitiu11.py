import random

def evaluate_function(x, y, z):
    t = x + y - z
    return t * x**2 - 2 * y * z

def generate_solution():
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    z = random.uniform(-2, 2)
    return x, y, z

def maximize_function(n):
    max_quality = float('-inf')

    for _ in range(n):
        x, y, z = generate_solution()
        quality = evaluate_function(x, y, z)
        if quality > max_quality:
            max_quality = quality

    return max_quality

n = int(input("Introduceti numarul de elemente pentru generare si evaluare: "))

max_quality = maximize_function(n)
print("Calitatea maxima gasita:", max_quality)
