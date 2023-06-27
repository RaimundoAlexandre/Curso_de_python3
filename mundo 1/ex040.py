n1 = float(input("Qual a primeira nota do aluno? "))
n2 = float(input("Qual a segunda nota do aluno? "))
media = (n1 + n2) / 2

if media < 5:
    print(f"A média é {media:.1f}")
    print("Reprovado")
elif media == 5 or media <= 6.9:
    print(f"A média é {media:.1f}")
    print("Recuperação")
elif media >= 7:
    print(f"A média é {media:.1f}")
    print("Aprovado", end=' ')
    print("Parabéns")

