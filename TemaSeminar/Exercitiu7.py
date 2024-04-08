def citire_lista():
    lista_str = input("Introduceti o lista de numere separate prin spatiu: ")
    lista = list(map(int, lista_str.split()))
    return lista
def sortare_insertie(lista):
    for i in range(1, len(lista)):
        element_curent = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > element_curent:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = element_curent
    return lista

lista = citire_lista()
print(f"Lista nesortata: {lista}")

lista_sortata = sortare_insertie(lista)
print(f"Lista sortata: {lista_sortata}")
