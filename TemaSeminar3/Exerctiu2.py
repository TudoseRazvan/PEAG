import numpy as np

def generare_populatie(dimensiune_populatie):
    return np.random.randint(2, size=(dimensiune_populatie, 5))

def calitate_individ(individ):
    numar_perechi_diferite = sum(1 for i in range(len(individ) - 1) if individ[i] != individ[i+1])
    return numar_perechi_diferite

def individ_cu_cea_mai_mare_calitate(populatie):
    valori_calitate = [calitate_individ(individ) for individ in populatie]
    index_max = np.argmax(valori_calitate)
    return populatie[index_max], valori_calitate[index_max]

#Generam o populatie de 18 indivizi
populatie = generare_populatie(18)

#Afișam populatia generata
print("Populatie generata:")
print(populatie)

#Identificam si afisam individul cu cea mai mare calitate
individ_max_calitate, valoare_max_calitate = individ_cu_cea_mai_mare_calitate(populatie)
print("\nIndivid cu cea mai mare calitate:")
print(individ_max_calitate)
print("Valoare calitate:", valoare_max_calitate)
