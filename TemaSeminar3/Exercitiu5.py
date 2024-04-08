import random

def genereaza_indivizi(n):
    indivizi = []
    numar_generat = 0

    while numar_generat < n:
        #Generarea unui vector binar aleatoriu de dimensiune 8
        individ = random.choices([0, 1], k=8)

        #Numararea bitilor 1
        numar_biti_1 = sum(individ)

        #Verificarea daca numarul de biti 1 este impar
        if numar_biti_1 % 2 == 1:
            #Calculul calitatii individului
            calitate = 0
            for i in range(8):
                calitate += individ[i] * (2 ** (7 - i))

            #Adaugarea individului si calitatii la lista
            indivizi.append((individ, calitate))
            numar_generat += 1

    return indivizi


while True:
    try:
        n = int(input("Introduceti numarul de indivizi (numar intreg pozitiv): "))
        if n > 0:
            break
        else:
            print("Numarul trebuie sa fie un numar intreg pozitiv.")
    except ValueError:
        print("Introduceti un numar intreg valid.")

indivizi = genereaza_indivizi(n)

for individ, calitate in indivizi:
    print(f"Individ: {individ}, Calitate: {calitate}")

calitate_maxima = max(calitate for individ, calitate in indivizi)

print(f"Calitate maxima: {calitate_maxima}")
print("Indivizi cu calitatea maxima:")
for individ, calitate in indivizi:
    if calitate == calitate_maxima:
        print(individ)
