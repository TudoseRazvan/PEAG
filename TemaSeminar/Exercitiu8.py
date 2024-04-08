def citire_permutare():
    permutare_str = input("Introduceți o permutare (numere separate prin spațiu): ")
    permutare = list(map(int, permutare_str.split()))
    return permutare

def este_permutare_identica(permutare):
  for i in range(len(permutare)):
    if permutare[i] != i:
      return False
  return True

permutare = citire_permutare()
print(f"Permutarea {permutare} este identică: {este_permutare_identica(permutare)}")