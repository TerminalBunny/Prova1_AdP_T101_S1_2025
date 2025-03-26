workedTime = int(input("Quantidade de horas trabalhadas no mês: "))
workSalary = float(input("Salário por hora: "))

if workedTime <= 40*4:
    payroll = workedTime * workSalary
else:
    normalPayroll = 40*4 * workSalary
    overtimePayroll = (workedTime - 40*4) * workSalary * 1.5
    payroll = normalPayroll + overtimePayroll

print(f"Salário bruto: R${payroll:.2f}")