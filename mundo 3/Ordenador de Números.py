#numeros = []

"""
for c in range(0, 5):
    num = int(input("Digite um valor: "))
    if c == 0 or num >= numeros[-1]:
        numeros.append(num)
    else:
        for i in range(len(numeros)):
            if num < numeros[i]:
                numeros.insert(i, num)
                break

print("=-=" * 10)
print(numeros)

"""

numeros = []  # Lista vazia para armazenar os valores

for c in range(0, 5):
    n = int(input("Digite um valor: "))

    # Condição para verificar se é o primeiro valor ou se o valor digitado é maior do que o último valor da lista
    if c == 0 or n > numeros[-1]:
        numeros.append(n)  # Adiciona o valor no final da lista
    else:
        pos = 0  # Variável para controlar a posição na lista
        while pos < len(numeros):
            # Verifica se o valor digitado é menor ou igual ao valor da posição atual na lista
            if n <= numeros[pos]:
                numeros.insert(pos, n)  # Insere o valor na posição adequada
                break
            pos += 1  # Incrementa a posição

print("=-="*10)
print(f"Os valores digitados em ordem foram: {numeros}")

