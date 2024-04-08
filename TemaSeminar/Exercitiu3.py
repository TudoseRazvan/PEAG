def citire_matrice():
    n = int(input("Introduceti numarul de linii: "))
    matrice = []
    for _ in range(n):
        linie = list(map(int, input().split()))
        matrice.append(linie)
    return matrice

def bubble_sort(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i]) - 1):
            for k in range(len(matrice[i]) - 1 - j):
                if matrice[i][k] > matrice[i][k + 1]:
                    matrice[i][k], matrice[i][k + 1] = matrice[i][k + 1], matrice[i][k]

matrice = citire_matrice()
bubble_sort(matrice)

for linie in matrice:
    print(*linie)

