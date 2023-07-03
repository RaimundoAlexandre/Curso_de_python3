pessoas = []  # Lista para armazenar as informações das pessoas

while True:
  dado = []  # Lista temporária para armazenar nome e peso de cada pessoa
  dado.append(str(input("Nome: ")))  # Solicita o nome da pessoa e adiciona à lista temporária
  dado.append(float(input("Peso: ")))  # Solicita o peso da pessoa e adiciona à lista temporária
  pessoas.append(dado[:])  # Adiciona a lista temporária à lista de pessoas

  sair = str(input("Quer continuar? [S/N] ")).strip().upper()  # Verifica se o usuário deseja continuar
  if sair == 'N':
    break  # Encerra o loop caso o usuário não queira continuar

total = len(pessoas)  # Obtém o total de pessoas cadastradas

maior = menor = pessoas[0]  # Inicializa a primeira pessoa como a maior e a menor

p_maior = []  # Lista para armazenar os nomes das pessoas com o maior peso
p_menor = []  # Lista para armazenar os nomes das pessoas com o menor peso

for p in pessoas:
  if p[1] > maior[1]:
    maior = p  # Atualiza a pessoa com o maior peso caso encontre uma pessoa com peso maior
    p_maior = [p[0]]  # Adiciona o nome da pessoa com o maior peso à lista p_maior
  elif p[1] == maior[1]:
    p_maior.append(p[0])  # Adiciona o nome da pessoa com o mesmo maior peso à lista p_maior
  elif p[1] < menor[1]:
    menor = p  # Atualiza a pessoa com o menor peso caso encontre uma pessoa com peso menor
    p_menor = [p[0]]  # Adiciona o nome da pessoa com o menor peso à lista p_menor
  elif p[1] == menor[1]:
    p_menor.append(p[0])  # Adiciona o nome da pessoa com o mesmo menor peso à lista p_menor

print(f"Foram cadastradas {total} pessoas")
print(f"O maior peso foi {maior[1]} kg, de: {', '.join(p_maior)}")
print(f"O menor peso foi {menor[1]} kg, de: {', '.join(p_menor)}")
