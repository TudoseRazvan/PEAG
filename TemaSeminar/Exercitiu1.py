def citire_matrice():
    n = int(input("Introduceti numarul de linii: "))
    matrice = []
    for i in range(n):
        linie = list(map(int, input().split()))
        matrice.append(linie)
    return matrice

def numar_linii_crescatoare(matrice):
    numar_linii = 0
    for i in range(len(matrice)):
        linie_in_ordine = True
        for j in range(1, len(matrice[i])):
            if matrice[i][j] < matrice[i][j-1]:
                linie_in_ordine = False
            break
        if linie_in_ordine:
            numar_linii += 1
    return numar_linii

matrice = citire_matrice()
numar_linii = numar_linii_crescatoare(matrice)
print(f"Numarul de linii cu elemente in ordine crescatoare: {numar_linii}")
