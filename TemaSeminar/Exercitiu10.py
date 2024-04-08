import random
def generare_vector_binar():
  #Genereaza un vector binar aleatoriu de lungime 7.
  return [random.randint(0, 1) for _ in range(7)]

def generare_matrice_si_vector(n):
  #Genereaza o matrice A cu n linii și 7 coloane de vectori binari aleatori și un vector V cu calitatea liniilor.
  A = [generare_vector_binar() for _ in range(n)]
  V = [sum(linie) for linie in A]
  return A, V

def sortare_matrice(A, V):
  #Sorteaza liniile matricei A in functie de valorile din V (ordine crescatoare).
  n = len(A)
  swapped = True
  while swapped:
    swapped = False
    for i in range(n - 1):
      if V[i] > V[i + 1]:
        A[i], A[i + 1] = A[i + 1], A[i]
        V[i], V[i + 1] = V[i + 1], V[i]  #Sortarea simultana a lui V pentru a mentine corelatia
        swapped = True
  return A

while True:
  try:
    n = int(input("Introduceti numarul de linii (sau 0 pentru iesire): "))
    if n == 0:
      break
    A, V = generare_matrice_si_vector(n)

    print(f"Matricea A originala:")
    print(A)
    print(f"Vectorul V original:")
    print(V)

    A_sortat = sortare_matrice(A, V)

    print(f"Matricea A sortata dupa V:")
    print(A_sortat)
    print(f"Vectorul V sortat:")
    print(V)
  except ValueError:
    print("Eroare: Introduceti un numar intreg valid.")

print("Program terminat.")
