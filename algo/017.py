from cmath import cos, pi, tan
from math import log2


x=float(input("Birinchi sonni kiriting= "))
y=float(input("Ikkinchi sonni kiriting= "))
a=2*tan(x+(pi/6))
b=1/3+(1+cos((y+x**2)+(y+x**2)))/2
c=log2(x**2+2)
f1=(a/b)+c
if(((1<=x)and(1<=y))and((x<=100)and(y<=100))):
    print("Natija= ", f1)
else:
    print("Kiritilgan sonlar qo'yilgan shartga to'g'iri kelmaydi. Boshqa son kiriting!")