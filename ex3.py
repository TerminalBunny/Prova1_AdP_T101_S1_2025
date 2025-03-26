num1 = int(input("Digite um número (1/3): "))
num2 = int(input("Digite um número (2/3): "))
num3 = int(input("Digite um número (3/3): "))

while num1 == num2 or num1 == num3 or num2 == num3:
    print("Números iguais! Digite novos números.")
    num1 = int(input("Digite um número (1/3): "))
    num2 = int(input("Digite um número (2/3): "))
    num3 = int(input("Digite um número (3/3): "))

big = num1
if num2 > big:
    middle = num1
    big = num2
else:
    middle = num2
if num3 > big:
   small = middle
   middle = big
   big = num3
elif num3 > middle:
    small = middle
    middle = num3
else:
    small = num3

print(f"Os valores em ordem decrescente: {big}, {middle}, {small}")
