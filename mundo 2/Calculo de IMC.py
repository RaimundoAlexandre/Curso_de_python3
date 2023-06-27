print("Calculo de IMC")
print("=-="*5)

# Definindo a função de cálculo do IMC
def calculo_imc():
    while True:
        try:
            # Solicitando altura e peso ao usuário
            altura = float(input("Informe sua altura (M): ").strip())
            print("=-="*5)
            peso = float(input("Informe seu peso (KG): ").strip())
            print("=-="*5)

            # Calculando o IMC
            imc = peso / (altura ** 2)
            print(f"Seu IMC é {imc:.2f}", end=' ')

            # Verificando a faixa de IMC e exibindo a mensagem correspondente
            if imc < 18.5:
                print("Você está abaixo do peso ideal!")
                print("=-="*5)
            elif imc >= 18.5 and imc < 25:
                print("Você está dentro do peso ideal!")
                print("=-="*5)
            elif imc >= 25 and imc <= 30:
                print("Você está em sobrepeso!")
                print("=-="*5)
            elif imc > 30 and imc <= 40:
                print("Você está com obesidade!")
                print("=-="*5)
            elif imc > 40:
                print("Você está com obesidade mórbida!")
                print("=-="*5)
        except ValueError:
            # Lidando com entrada inválida de valores não numéricos
            print("Valores inválidos, informe valores numéricos separados por '.'")
            print("Exemplo: altura 1.78\npeso 1.66")
            print("=-="*5)
        
        # Verificando se o usuário deseja continuar
        sair = input("Deseja continuar?\nDigite 'S' para sim e 'N' para não: ").upper().strip()
        if sair == 'N':
                # Encerrando a execução do programa
                break                        
        elif sair != 'S': # Lidando com entrada inválida para a pergunta de continuação
            print("Valor inválido\nO programa será encerrado")
            break

# Chamando a função para iniciar o cálculo do IMC
calculo_imc()
