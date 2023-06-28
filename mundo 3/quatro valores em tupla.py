n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
n4 = int(input("Digite o quarto valor: "))
print("=-="*10)

valores = (n1, n2, n3, n4)

#print(valores)
#print("=-="*10)

print(f"O número 9 apareceu {valores.count(9)} vezes")
print("=-="*10)

if 3 in valores:
  print(f"O número 3 apareceu na posição {valores.index(3)}°")
  print("=-="*10)
else:
  print(f"O número 3 não apareceu em nenhuma posição")
  print("=-="*10)

print("Os números pares são ",end='')
"""
cont = 0 ### mesma solução do codigo a baixo, porem mais feio
for c in (valores):    
    if valores[cont] % 2 == 0:
        print(" ➟ ",end=' ')         
        print(f"{valores[cont]} ",end='')
    cont += 1
"""
for valor in (valores): ### forma mais limpa e clara
    if valor % 2 == 0:
        print(" ➟ ",end=' ')
        print(f"{valor} ",end='')

