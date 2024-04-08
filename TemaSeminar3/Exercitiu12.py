import random

def genereaza_indivizi():
  indivizi = []
  for _ in range(10):
    #Generarea individului
    individ = []
    for _ in range(8):
      individ.append(random.randint(0, 1))

    #Calculul calitatii individului
    calitate = 0
    for i in range(0, 8, 2):
      if individ[i] == 1:
        calitate += 1

    #Adaugarea individului si calitatii la matrice
    indivizi.append((individ, calitate))

  return indivizi

indivizi = genereaza_indivizi()

for i in range(10):
  print(f"Individ {i + 1}: {indivizi[i][0]}, Calitate: {indivizi[i][1]}")

calitate_medie = sum(calitate for individ, calitate in indivizi) / 10

print(f"Calitate medie: {calitate_medie}")
