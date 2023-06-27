numero = ('zero','um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete','oito',
          'nove','dez','onze','doze','treze','quatorze','quinze','dezeseis',
          'dezesete','dezoite','dezenove','vinte')

num = int(input("Digite um número inteiro entre '0' e '20': "))

while True:
  if num >= 0 and num <= 20:
    print(numero[num])
    break
  else:
    num = int(input("Tente novamente, digite um número inteiro entre '0' e '20': "))
