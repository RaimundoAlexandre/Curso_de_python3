listaP = list()
soma = 0
while True:
  pessoa = dict()
  pessoa['nome'] = str(input("Nome: ")).strip().capitalize()
  pessoa['sexo'] = str(input("Sexo:[F/M] ")).strip().upper()[0]
  
  while not pessoa['sexo'] in 'FM':
    print("ERRO. Porfavor digite apenas F ou M")
    pessoa['sexo'] = str(input("Sexo:[F/M] ")).strip().upper()[0]
    
  pessoa['idade'] = int(input("Idade: "))
  listaP.append(pessoa)
  soma += pessoa['idade']
  
  sair = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
  while not sair in 'SN':
    print("ERRO. Porfavor digite apenas S ou N")
    sair = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
  if sair == 'N':
    break
    
print("=-="*10)
media = soma/len(listaP)
print(f"Foram cadastradas {len(listaP)} pessoas")
print(f"A media de idade é {media}")
print("As mulheres cadastradas foram ",end=' ')

for p in listaP:
  if p['sexo'] == 'F':
    print(f"{p['nome']}", end=' ')
print()
print("=-="*10)
print("↓ As pessoas acima da media foram ↓")
for p in listaP:
  if p['idade'] >= media:
    print("   ",end='')
    for k, v in p.items():
      print(f"{k} = {v}; ", end ='')
    print()
print("=-="*10)
print("<<< ENCERRADO >>>")
