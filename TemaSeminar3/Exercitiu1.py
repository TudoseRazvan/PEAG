import random

def f(x, y, z):
  return x**2 - 2 * y * z

#Generarea a 20 de candidati la solutie
candidati = []
for _ in range(20):
  x = random.uniform(-2, 7)
  y = random.uniform(-2, 7)
  z = random.uniform(-2, 7)
  while x + y + z >= 10:
    x = random.uniform(-2, 7)
    y = random.uniform(-2, 7)
    z = random.uniform(-2, 7)
  candidati.append((x, y, z))

#Evaluarea functiei f pentru candidatii la solutie
valori = [f(x, y, z) for x, y, z in candidati]

#Afisarea valorilor obtinute
for i, (x, y, z) in enumerate(candidati):
  print(f"Candidat {i+1}: ({x:.2f}, {y:.2f}, {z:.2f}) -> f = {valori[i]:.2f}")

#Gasirea maximului
valoare_max = max(valori)
indice_max = valori.index(valoare_max)
x_max, y_max, z_max = candidati[indice_max]

print(f"\nSolutia optima: ({x_max:.2f}, {y_max:.2f}, {z_max:.2f}) -> f = {valoare_max:.2f}")