ano = int(input("Qual a idade do atleta? "))

if ano <= 9:
    print("Mirim")
elif ano > 9 and ano <= 14:
    print("Infantil")
elif ano > 14 and ano <= 19:
    print("Junior")
elif ano > 19 and ano <= 20:
    print("Sénior")
elif ano > 20:
    print("Master")
