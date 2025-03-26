birthYear = int(input("Ano de nascimento: "))
birthday = "NaV"

while birthday != "S" and birthday != "N":
    birthday = (input("Já fez aniversário esse ano (S/N)?: "))
    if birthday != "S" and birthday != "N":
        print("Resposta inválida. Informe 'S' para sim ou 'N' para não.")
currentYear = 2025
if birthday == "S":
    ageYear = currentYear - birthYear
else:
    ageYear = (currentYear-1) - birthYear

ageDay = ageYear*365
ageMonth = ageDay//30

print(f"Você tem aproximadamente {ageYear} anos, {ageMonth} meses e {ageDay} dias de vida")