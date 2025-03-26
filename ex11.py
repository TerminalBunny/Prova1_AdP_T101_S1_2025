people = 0
salaryBig = 0
salarySum = 0
childrenSum = 0
lessWage = 0
salary = 0

while salary >= 0:
    print(f"PESSOA {people+1}")
    salary = float(input("Salário (número negativo para parar): "))
    if salary >= 0:
        children = int(input("Nº de Filhos: "))
        salarySum += salary
        childrenSum += children
        if salary > salaryBig:
            salaryBig = salary
        if salary < 1500.00:
            lessWage += 1
        people += 1

salaryAvg = salarySum/people
childrenAvg = childrenSum/people
lessWagePctg = lessWage/people

print(f"Média de salário: R${salaryAvg:.2f}")
print(f"Média de filhos: {childrenAvg:.2f}")
print(f"{lessWagePctg*100:.2f}% das pessoas ganham menos de R$1500.00")
print(f"Maior salário: R${salaryBig:.2f}")