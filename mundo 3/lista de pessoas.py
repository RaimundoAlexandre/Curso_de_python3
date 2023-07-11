import pandas as pd

mulheres = []
acimaMedia = []
sair = ''
cont = 0
soma = 0

while sair != 'N':
  acimaM = {}
  feminino = {}
  nome = str(input("Nome: ")).strip().capitalize()
  cont += 1
  sexo = str(input("Sexo:[F/M] ")).strip().upper()[0]
  while sexo not in 'FM':
    print("ERRO! responda apenas F ou M")
    sexo = str(input("Sexo:[F/M] ")).strip().upper()[0]
    
  idade = int(input("Idade: "))
  soma += idade
  if sexo == 'F':
    feminino['nome'] = nome
    feminino['sexo'] = sexo
    feminino['idade'] = idade
    mulheres.append(feminino)
    
  media = (soma/cont)
  if idade > media:
    acimaM['nome'] = nome
    acimaM['sexo'] = sexo
    acimaM['idade'] = idade
    acimaMedia.append(acimaM)
  sair = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
  while sair not in 'SN':
    print("ERRO! responda apenas S ou N")
    sair = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
  print("=-="*10)
  
print(f"O grupo tem {cont} pessoas")
print(f"A media de idade é {media}") 
tabelaMedia = pd.DataFrame(acimaMedia)
print(f"lista de pessoas acima da media\n{tabelaMedia}")
print("lista de mulheres")
tabelaF = pd.DataFrame(mulheres)
print(tabelaF)
