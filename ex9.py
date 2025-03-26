sum = 0

for i in range(10):
    number = float(input(f"Digite um número ({i+1}/10): "))
    sum += number
avg = sum/(i+1)

print(f"A média dos 10 números é {avg:.2f}")