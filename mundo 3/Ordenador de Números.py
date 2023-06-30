numeros = []
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
