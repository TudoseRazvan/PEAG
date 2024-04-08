import random

def generare_vector_binar():
#Generează un vector binar aleatoriu de lungime 7.
    return [random.randint(0, 1) for _ in range(7)]

def generare_matrice_si_vector(n):
#Generează o matrice A cu n linii și 7 coloane de vectori binari aleatori și un vector V cu calitatea liniilor.
    A = [generare_vector_binar() for _ in range(n)]
    V = [sum(linie) for linie in A]
    return A, V

while True:
  try:
    n = int(input("Introduceti numarul de linii (sau 0 pentru ieșire): "))
    if n == 0:
      break
    A, V = generare_matrice_si_vector(n)

    print(f"Matricea A:\n{A}")
    print(f"Vectorul V:\n{V}")
  except ValueError:
    print("Eroare: Introduceti un numar intreg valid.")

print("Program terminat.")
