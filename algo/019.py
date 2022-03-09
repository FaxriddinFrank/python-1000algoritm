from asyncio import log
from cmath import cos, e
from math import log1p, log2


x=int(input("Birinchi sonni kiriting= "))
y=int(input("Ikkinchi sonni kiriting= "))
a=(log2(abs((x+y)**2+(abs(y)+2)**(1/2))-(x-((x*y)/((x**2/2)-5)))))/(log2(e))
c=((1+cos((x+y)*(x+y)))/2)/((x+y)**(1/3))
f2=a+c
if(((1<=x)and(1<=y))and((x<=10)and(y<=10))):
    print("Natija= ", f2)
else:
    print("Kiritilgan sonlar qo'yilgan shartga to'g'iri kelmaydi. Boshqa son kiriting!")