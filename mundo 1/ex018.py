from math import sin, cos, tan, radians

ang = float(input("Digite um angolo para saber seu seno, cosseno e tangent: "))

seno = sin(radians(ang))
coseno = cos(radians(ang))
ta = tan(radians(ang))

print("O seno de {} é {:.2f} \nO cosseno é {:.2f} \nA tangente é {:.2f}".format(ang, seno, coseno, ta))
