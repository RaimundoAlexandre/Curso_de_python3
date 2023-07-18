import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print("ERROR!")
else:
    print("Tudo OK")
