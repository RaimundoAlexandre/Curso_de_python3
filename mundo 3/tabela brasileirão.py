futebol = ('Flamengo', 'Palmeiras','Athletico Paranaense','Atlético Mineiro','São Paulo','Fluminense',
           'Fortaleza','Corinthians','Santos','Internacional','Grêmio',
           'América Mineiro','Atlético Goianiense','Ceará','Bahia','Botafogo','Red Bull Bragantino','Cruzeiro',
           'Goiás','Cuiabá')

print(f"Os 5 primeiros colocados da CBF são{futebol[0:5]}")
print("=-="*20)
print(f"Os ultimos 4 colocados da CBF são {futebol[16:]}")
print("=-="*20)
print(f"Os times da CBF em ordem alfabetica {sorted(futebol)}")
print("=-="*20)
print(f"O Ceará esta na {futebol.index('Ceará')}° posição")
