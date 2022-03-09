from cmath import e
from tkinter import E


x=float(input("Birinchi sonni kiriting= "))
y=float(input("Ikkinchi sonni kiriting= "))
c1=(x+y)/(y**2+abs((y**2+2)/(x+((x**3)/5))))+(e**(y+2))
if(((1<=x)and(1<=y))and((x<=100)and(y<=100))):
    print("Natija= ", c1)
else:
    print("Kiritilgan son qo'yilgan shartga to'g'iri kelmaydi. Boshqa son kiriting!")