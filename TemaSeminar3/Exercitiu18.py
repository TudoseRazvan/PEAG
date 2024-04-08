import numpy as np

def evaluate_solution(solution):
    x1, x2, x3, x4, x5, x6, x7, x8 = solution
    return x1 + x2 + x3 + x4 - (x5 + x6 + x7 + x8)

def generate_solutions(n):
    solutions = []
    for _ in range(n):
        #Generam o solutie aleatoare cu valori -1 si 1
        solution = np.random.choice([-1, 1], size=8)
        solutions.append(solution)
    return solutions

def print_solutions(solutions):
    for idx, solution in enumerate(solutions):
        print(f"Sol: {solution} - Calitate: {evaluate_solution(solution)}")

def find_max_quality(solutions):
    max_quality = float('-inf')
    for solution in solutions:
        quality = evaluate_solution(solution)
        if quality > max_quality:
            max_quality = quality
    return max_quality

n = int(input("Introduceti numarul de solutii (n): "))

solutions = generate_solutions(n)
print("Solutiile generate:")
print_solutions(solutions)

max_quality = find_max_quality(solutions)
print(f"\nCalitatea maxima a solutiilor: {max_quality}")
