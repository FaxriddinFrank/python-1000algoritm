from cmath import cos, log, sin
from tkinter import ARC


x=float(input("Birinchi sonni kiriting= "))
y=float(input("Ikkinchi sonni kiriting= "))
a=y**2+(y+y*x)/(abs(x*y)+5)
b=x*y+y**2
c=x**2+a/b+log(e(4))
d=(x**2+1)/c
e=1/(1+cos(x)+(1/sin(abs(x))))
T11=d+e
if(((1<=x)and(1<=y))and((x<=30)and(y<=30))):
    print("Natija= ", T11)
else:
    print("Kiritilgan sonlar qo'yilgan shartga to'g'iri kelmaydi. Boshqa son kiriting!")