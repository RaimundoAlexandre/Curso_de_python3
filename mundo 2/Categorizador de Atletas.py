from datetime import datetime

print("=-=-=" * 10)

# Loop para solicitar o ano de nascimento
while True:
    try:
        ano = input("Em que ano você nasceu? EX: 1992. ")
        
        # Verifica se a entrada tem 4 dígitos
        if len(ano) != 4:
            raise ValueError  # Levanta uma exceção para tratar a entrada inválida
        
        ano = int(ano)  # Converte a entrada para um número inteiro
        break  # Sai do loop quando a entrada é válida
    
    except ValueError:
        print("Valor inválido. Por favor, digite um ano válido com 4 dígitos.")

MIRIM_IDADE_MAXIMA = 9
INFANTIL_IDADE_MAXIMA = 14
JUNIOR_IDADE_MAXIMA = 19
SENIOR_IDADE_MAXIMA = 20

print("=-=-=" * 10)

# Obtém o ano atual
ano_atual = datetime.now().year

# Calcula a idade
idade = ano_atual - ano

categoria = ""

# Determina a categoria com base na idade
if idade <= MIRIM_IDADE_MAXIMA:
    categoria = "mirim"
elif idade <= INFANTIL_IDADE_MAXIMA:
    categoria = "infantil"
elif idade <= JUNIOR_IDADE_MAXIMA:
    categoria = "júnior"
elif idade <= SENIOR_IDADE_MAXIMA:
    categoria = "sênior"
else:
    categoria = "master"

# Exibe a idade e a categoria do atleta
print(f"Você tem {idade} anos. O atleta está na categoria {categoria}.")
print("=-=-=" * 10)
