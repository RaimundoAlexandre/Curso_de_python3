import urllib
import urllib.request
site=str('Insira o site: ')
try:
    site1=urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('O Site não está acessível no momento')
else:
    print('Consegui abrir o site com sucesso!')
