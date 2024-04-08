import random

def generate_permutations(n):
    permutations = []

    for _ in range(n):
        # Generăm o permutare aleatorie de dimensiune 8
        permutation = random.sample(range(8), 8)

        # Calculăm calitatea permutării
        quality = 0
        for i in range(8):
            for j in range(i + 1, 8):
                if permutation[i] == j and permutation[j] == i:
                    quality += 1

        permutations.append((permutation, quality))

    return permutations


while True:
    try:
        n = int(input("Introduceti numarul de indivizi (numar intreg pozitiv): "))
        if n > 0:
            break
        else:
            print("Numarul trebuie sa fie un numar intreg pozitiv.")
    except ValueError:
        print("Introduceti un numar intreg valid.")

permutations = generate_permutations(n)

for permutation, quality in permutations:
    print(f"Permutare: {permutation}, Calitate: {quality}")

max_quality = max(quality for _, quality in permutations)

print(f"Valoarea maxima a calitatii este: {max_quality}")
