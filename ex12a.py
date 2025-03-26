s1 = 1
s2 = 2
n = int(input("Qual termo quer saber?: "))
if n == 1:
    s = 1
elif n == 2:
    s = 2
else:
    for count in range(n-2):
        s = (2*s2)+s1
        s1 = s2
        s2 = s
print(s)