aluno = {}

aluno['nome'] = str(input("Nome: ")).strip().capitalize()
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
print(f"O aluno {aluno['nome']} tem media {aluno['media']}",end=' ')

if aluno['media'] >= 7:
  print("Aprovado")
else:
  print("Reprovado")