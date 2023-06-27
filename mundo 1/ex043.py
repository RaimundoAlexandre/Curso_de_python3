peso = float(input('Digite o seu peso Kg:'))
altura = float(input('Digite sua altura M: '))

IMC = peso / (altura ** 2)

print('Seu IMC é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você esta abaixo do peso ideal')
elif 18.5 <= IMC < 25:
    print('Você esta no peso ideal')
elif 25 <= IMC < 30:
    print('Você esta com sobre peso')
elif 30 <= IMC < 40:
    print('Voce esta com obesidade')
elif IMC > 40:
    print('Você esta com obesidade morbida')
