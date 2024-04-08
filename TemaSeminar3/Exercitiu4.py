import random

def calculate_quality(permutation):
    quality = 0
    for i in range(len(permutation)):
        for j in range(i + 1, len(permutation)):
            if abs(i - j) % 2 == 0 and abs(permutation[i] - permutation[j]) % 2 == 0:
                quality += 1
    return quality

def generate_permutations(k, n):
    permutations = []

    for _ in range(n):
        permutation = list(range(k))
        random.shuffle(permutation)
        quality = calculate_quality(permutation)
        permutations.append((permutation, quality))

    return permutations

while True:
    try:
        k = int(input("Introduceti dimensiunea permutarilor (numar intreg pozitiv): "))
        if k > 0:
            break
        else:
            print("Dimensiunea trebuie să fie un numar intreg pozitiv.")
    except ValueError:
        print("Introduceti un numar intreg valid.")

n = 15
permutations = generate_permutations(k, n)

for permutation, quality in permutations:
    print(f"Permutare: {permutation}, Calitate: {quality}")

max_quality = max(permutation[1] for permutation in permutations)

print(f"Valoarea maxima a calitatii este: {max_quality}")
