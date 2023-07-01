galera = list()  # Lista para armazenar as informações de cada pessoa
dado = list()  # Lista temporária para coletar nome e idade de cada pessoa

# Loop para coletar informações de 5 pessoas
for c in range(0, 5):
    dado.append(str(input("Nome: ")))  # Coleta o nome da pessoa
    dado.append(int(input("Idade: ")))  # Coleta a idade da pessoa
    galera.append(dado[:])  # Adiciona uma cópia dos valores coletados à lista "galera"
    dado.clear()  # Limpa a lista "dado" para a próxima iteração

maior = menor = 0  # Variáveis para contar o número de maiores e menores de idade

# Loop para categorizar e exibir as informações de cada pessoa
for p in galera:
    if p[1] >= 21:  # Verifica se a idade é maior ou igual a 21
        print(f"{p[0]} é maior de idade e tem {p[1]} anos")
        maior += 1  # Incrementa a contagem de maiores de idade
    else:
        print(f"{p[0]} é menor de idade e tem {p[1]} anos")
        menor += 1  # Incrementa a contagem de menores de idade

# Exibe a contagem final de maiores e menores de idade
print(f"Temos {maior} maiores de idade e {menor} menores de idade")
