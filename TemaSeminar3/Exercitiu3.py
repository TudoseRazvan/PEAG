import numpy as np
def maxim(a, n):
  #Generarea a n elemente aleatorii din spatiul solutiilor
  solutions = generate_solutions(n)

  #Evaluarea functiei f pentru fiecare element generat
  values = [f(solution, a) for solution in solutions]

  #Calculul mediei valorilor funcției f
  mean = sum(values) / n

  return mean

def f(x, a):
  sum_x = sum(x[:-1])
  return sum(a_i * x_i for a_i, x_i in zip(a, x))

def generate_solutions(n):
  solutions = np.random.randint(-1, 2, (n, 10))
  #Se verifica daca suma primelor 9 elemente este egală cu 1 - ultimul element
  for i in range(n):
    while sum(solutions[i, :-1]) != 1 - solutions[i, -1]:
      solutions[i, :] = np.random.randint(-1, 2, (10,))

  return solutions

a = list(map(int, input("Introduceti elementele vectorului a (separate prin spatiu): ").split()))

n = 10

mean = maxim(a, n)

print(f"Valoarea medie a funcției f este: {mean}")
