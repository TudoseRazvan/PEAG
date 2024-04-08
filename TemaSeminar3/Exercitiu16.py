import numpy as np

def calculate_quality(permutation):
    quality = sum(1 for i in range(6) if permutation[i] == i+1 and permutation[i+1] == i)
    return quality

def generate_permutations_and_quality(n):
    max_quality = 0
    for _ in range(n):
        #Generam o permutare aleatoare de dimensiune 7
        permutation = np.random.permutation(7)
        quality = calculate_quality(permutation)
        if quality > max_quality:
            max_quality = quality
        print(f"Permutarea: {permutation} - Calitate: {quality}")
    print(f"Valoarea maxima a calitatii: {max_quality}")

n = int(input("Introduceti numarul de permutari (n): "))

generate_permutations_and_quality(n)
