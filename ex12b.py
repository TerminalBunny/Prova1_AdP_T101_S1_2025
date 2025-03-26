s1 = 1
s2 = 2
soma = s1 + s2
n = int(input("Qual termo quer saber?: "))
if n == 1:
    s = 1
    soma = soma - s2
elif n == 2:
    s = 2
    soma = soma
else:
    for count in range(n-2):
        s = (2*s2)+s1
        soma += s
        s1 = s2
        s2 = s
print(f"{n}º Termo: {s}")
print(f"Soma de todos os elementos até {n}: {soma}")