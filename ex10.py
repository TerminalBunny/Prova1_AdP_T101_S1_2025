sum = 0

numberStudents = int(input("Quantidade de alunos na turma: "))
for i in range(numberStudents):
    grade = float(input(f"Nota do aluno {i+1} de {numberStudents}: "))
    sum += grade
avg = sum/numberStudents

print(f"Média das notas dos alunos: {avg:.2f}")