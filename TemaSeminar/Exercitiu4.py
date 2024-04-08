def citire_matrice():
    n = int(input("Introduceti numarul de linii: "))
    matrice = []
    for _ in range(n):
        linie = list(map(int, input().split()))
        matrice.append(linie)
    return matrice

def sortare_insertie(matrice):
    for j in range(len(matrice[0])):
        for i in range(1, len(matrice)):
            element_curent = matrice[i][j]
            k = i - 1
            while k >= 0 and matrice[k][j] > element_curent:
                matrice[k + 1][j] = matrice[k][j]
                k -= 1
            matrice[k + 1][j] = element_curent

matrice = citire_matrice()
sortare_insertie(matrice)

for linie in matrice:
    print(*linie)

