from ast import arg
from cmath import cos, e, tan
from tkinter import ARC


x=float(input("Birinchi sonni kiriting= "))
y=float(input("Ikkinchi sonni kiriting= "))
a=1/(x+(2/(x**2))+(3/(x**3)))+e**(x**2+3*x)
b=ARC(tan((x+y)+abs(5+x)**2))
c=(1+cos((y**2+(x**2)/2)*(y**2+(x**2)/2)))/2
f2=(a/b)+c
if(((1<=x)and(1<=y))and((x<=10)and(y<=10))):
    print("Natija= ", f2)
else:
    print("Kiritilgan sonlar qo'yilgan shartga to'g'iri kelmaydi. Boshqa son kiriting!")