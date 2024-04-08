def citire_matrice(n):
  matrice = []
  for _ in range(n):
    linie = list(map(int, input().split()))
    matrice.append(linie)
  return matrice

def transpusa(matrice):
  transpusa = []
  for i in range(len(matrice[0])):
    linie = [matrice[j][i] for j in range(len(matrice))]
    transpusa.append(linie)
  return transpusa

def suma_matrice(A, B):
  suma = []
  for i in range(len(A)):
    linie = [A[i][j] + B[i][j] for j in range(len(A[0]))]
    suma.append(linie)
  return suma

def produs_matrice(A, B):
  produs = []
  for i in range(len(A)):
    linie = []
    for j in range(len(B[0])):
      suma = 0
      for k in range(len(A[0])):
        suma += A[i][k] * B[k][j]
      linie.append(suma)
    produs.append(linie)
  return produs

def putere_matrice(A, n):
  if n == 1:
    return A
  else:
    return produs_matrice(A, putere_matrice(A, n - 1))

def afisare_matrice(matrice):
  for linie in matrice:
    print("[", end="")
    for element in linie:
      print(f" {element}", end="")
    print("]")

n = int(input("Introduceti dimensiunea matricelor: "))
A = citire_matrice(n)
B = citire_matrice(n)

print("Transpusa lui A:")
afisare_matrice(transpusa(A))

print("Suma A + B:")
afisare_matrice(suma_matrice(A, B))

print("Produsul A * B:")
afisare_matrice(produs_matrice(A, B))

print(f"Puterea A^{n}:")
afisare_matrice(putere_matrice(A, n))