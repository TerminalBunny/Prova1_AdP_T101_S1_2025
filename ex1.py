a = float(input("Digite um valor para 'a': "))
b = float(input("Digite um valor para 'b': "))
c = float(input("Digite um valor para 'c': "))

sum = a + b
print(f"a + b = {sum:.2f}")

if sum < c:
    print("a + b é menor que c")
else:
    print("a + b não é menor que c")