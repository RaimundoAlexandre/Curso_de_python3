aluno = {}

aluno['Nome'] = str(input("Nome do aluno: ")).strip().capitalize()
aluno['Media'] = float(input("Media do aluno "))
print("=-="*10)

print(f"O nome do aluno é {aluno['Nome']}")

if aluno['Media'] >= 7:
    print(f"Media {aluno['Media']} Aprovado")
else:
    print(f"Media {aluno['Media']} Reprovado")
