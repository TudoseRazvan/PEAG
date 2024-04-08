import math
import random

def functie_obiectiv(x):
  #Calculează valoarea funcției obiectiv pentru un fenotip dat
  return (math.sin(x - 2)) ** 2 - x * math.cos(x)

def genereaza_vecini(sir_binar):
  #Genereaza toti vecinii cu distanta Hamming 1 si fenotipuri valide
  vecini = []
  for i in range(len(sir_binar)):
    sir_nou = list(sir_binar)
    sir_nou[i] = str(1 - int(sir_binar[i]))
    fenotip_nou = int(''.join(sir_nou), 2)
    if 1 <= fenotip_nou <= 2500:
      vecini.append(''.join(sir_nou))
  return vecini

def hill_climbing(max_i=100000):
  #Efectuează hill climbing pentru a găsi un maxim local
  sir_binar = format(random.randint(1, 2500), 'b')
  valoare_curenta = functie_obiectiv(int(sir_binar, 2))
  for _ in range(max_i):
    imbunatatit = False
    for vecin in genereaza_vecini(sir_binar):
      valoare_vecin = functie_obiectiv(int(vecin, 2))
      if valoare_vecin > valoare_curenta:
        sir_binar = vecin
        valoare_curenta = valoare_vecin
        imbunatatit = True
    if not imbunatatit:
      break
  return sir_binar, valoare_curenta

  #Ruleaza algoritmul
cel_mai_bun_sir, cea_mai_buna_valoare = hill_climbing()

  #Afiseaza rezultatele
print("Cel mai bun sir binar:", cel_mai_bun_sir)
print("Fenotipul corespunzator:", int(cel_mai_bun_sir, 2))
print("Cea mai buna valoare a functiei obiectiv:", cea_mai_buna_valoare)
