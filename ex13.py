people = 3
oldPeople = 0
newHeightSum = 0
youngPeople = 0
petitPeople = 0
avgYoungHeight = 0

for count in range(people):
    age = int(input("Idade: "))
    height = int(input("Altura (em m): "))
    weight = int(input("Peso (em kg): "))
    if age >= 50:
        oldPeople += 1
    if age >= 10:
        if age <=20:
            newHeightSum += height
            youngPeople += 1
    if weight < 40:
        petitPeople += 1

print("############################################################")
if oldPeople == 0:
    print("Maiores de 50 anos: NÃO HÁ")
else:
    print(f"Maiores de 50 anos: {oldPeople}")
if youngPeople == 0:
    print("Altura média entre 10 e 20 anos: NÃO HÁ")
else:
    avgYoungHeight = newHeightSum/youngPeople
    print(f"Altura média entre 10 e 20 anos: {avgYoungHeight:.2f}")
petitPctg = (petitPeople/people)*100
print(f"Pessoas abaixo de 40kg: {petitPctg:.2f}%")