def citire_matrice():
    n = int(input("Introduceti numarul de linii: "))
    matrice = []
    for _ in range(n):
        linie = list(map(int, input().split()))
        matrice.append(linie)
    return matrice

def coloane_cu_minim_5(matrice):
    coloane_min_5 = []
    for j in range(len(matrice[0])):
        min_col = min(matrice[i][j] for i in range(len(matrice)))
        if min_col == 5:
            coloane_min_5.append(j)
    return coloane_min_5

matrice = citire_matrice()
coloane_min_5 = coloane_cu_minim_5(matrice)

if not coloane_min_5:
    print("Nu exista coloane cu cel mai mic element egal cu 5.")
else:
    print(f"Coloane cu cel mai mic element egal cu 5: {coloane_min_5}")

