print("###### Mercadinho ######\n")
totalGasto = 0
acimaDeMil = 0
maisBarato = 0
nome = ''
cont = 0

while True:
    cont += 1
    produto = str(input("Nome do produto: ")).strip().capitalize()
    
    try:
        preco = float(input("Preço do produto: R$ "))
        
        if cont == 1:
            maisBarato = preco
            nome = produto
        elif maisBarato > preco:
            maisBarato = preco
            nome = produto

        print("=-=" * 10)
        totalGasto += preco
        
        if preco > 1000:
            acimaDeMil += 1
        
        sair = str(input("Quer continuar? [S/N]: ")).strip().upper()
        print("=-=" * 10)
        
        if sair in 'SN':
            if sair == 'N':
                break
        else:
            print("Valor inválido! Digite [S] para continuar ou [N] para encerrar.")
            sair = str(input("Quer continuar? [S/N]: ")).strip().upper()
            
            if sair == 'N':
                break
    except ValueError:
        print("Valor incorreto! Digite apenas números. Exemplo: 5.00")

print("###### Fim do programa ######\n")
print(f"O total gasto na compra foi R${totalGasto:.2f}")
print(f"Foram comprados {acimaDeMil} produtos que custam mais de R$1000.00")
print(f"O produto mais barato comprado foi '{nome}' que custou R${maisBarato:.2f}")
