from math import pow, sqrt, hypot

ca = float(input("Qual o comprimento do cateto oposto? "))
co = float(input("Qual o comprimento do cateto adjacente? "))

ipo = hypot(ca, co)   #pow(ca, 2) + pow(co, 2)

#print("A hipotenusa é {:.3f}".format(sqrt(ipo)))
print("A hipotenusa é {:.3f}".format(ipo))
