def cmmdc_recursiv(a, b):
    if b == 0:
        return a
    else:
        return cmmdc_recursiv(b, a % b)

a = int(input("Introduceti primul numar: "))
b = int(input("Introduceti al doilea numar: "))

cmmdc = cmmdc_recursiv(a, b)
print(f"CMMDC al lui {a} și {b} este: {cmmdc}")
