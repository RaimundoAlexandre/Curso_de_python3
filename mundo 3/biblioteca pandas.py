import pandas as pd

lista= [{'nome':'Alex','idade':31,'sexo':'M'},{'nome':'Jucy','idade':33,'sexo':'F'},{'nome':'Manoel','idade':22,'sexo':'M'},{'nome':'Clara','idade':13,'sexo':'F'},{'nome':'Jorel','idade':23,'sexo':'M'},{'nome':'Carlos','idade':42,'sexo':'M'},{'nome':'Maria','idade':33,'sexo':'F'}]
tabela = pd.DataFrame(lista)

print(tabela)