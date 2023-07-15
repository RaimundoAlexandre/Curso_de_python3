from datetime import datetime as dt


def voto(ano):
    data = dt.now().year
    idade = (data - ano)
    if 18 <= idade <= 65:
        obrigatorio = f"Com {idade} anos o voto é Obrigatorio"
        return obrigatorio
    elif 17 > idade < 65:
        facultativo = f"Com {idade} anos o voto é opicional"
        return facultativo
    elif idade > 16:
        negado = f"Com {idade} anos o voto sera negado"
        return negado


ano = int(input("Ano de nascimento: "))
situacao = voto(ano)
print(situacao)
