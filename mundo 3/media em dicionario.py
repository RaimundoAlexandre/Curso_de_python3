import pandas as pd
aluno = {}

aluno['nome'] = str(input("Nome: ")).strip().capitalize()
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
print("=-="*10)
#print(f"O aluno {aluno['nome']} tem media {aluno['media']}",end=' ')
print(f"Informações do aluno\n")

# if aluno['media'] >= 7:
#   print("Aprovado")
# elif 5 <= aluno['media'] < 7:
#   print("Recuperação")
# else:
#   print("Reprovado")
situacao = []
if aluno['media'] >= 7:
  aluno['situação'] = 'Aprovado'
  situacao.append(aluno)
  resultado = pd.DataFrame(situacao)
  print(resultado)
elif 5 <= aluno['media'] < 7:
  aluno['situação'] = 'Recuperação'
  situacao.append(aluno)
  resultado = pd.DataFrame(situacao)
  print(resultado)
else:
  aluno['situação'] = 'Reprovado'
  situacao.append(aluno)
  resultado = pd.DataFrame(situacao)
  print(resultado)