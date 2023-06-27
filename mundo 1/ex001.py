print("Ola Mundo")
def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('Valor invalido')

n1 = input_float('Primeiro número: ')
n2 = input_float('Segundo número: ')
print(n1 / n2)
