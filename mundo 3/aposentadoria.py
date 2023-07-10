from datetime import date

anoAtual = date.today().year

trabalhador = {}
trabalhador['nome'] = str(input("Nome: ")).strip().capitalize()
idade = int(input("Ano de nascimento: "))
trabalhador['idade'] = anoAtual - idade
trabalhador['ctps'] = int(input("Carteira de trabalho (0 não tem): "))
if trabalhador["ctps"] != 0:
  trabalhador['contratação'] = int(input("Ano de contratação: "))
  trabalhador['salario'] = int(input("Salário: R$ "))
  
  trabalhador['aposentadoria'] = (trabalhador['contratação'] - idade) + 35
print("=-="*10) 

for k, v in trabalhador.items():
  print(f"{k} tem o valor {v}")
