n=int(input("uch xonali son kiriting:"))
a=n%100
b=n//100
d=a*10+b
if((n>99)and(n<1000)):
    print("hosil bo'lgan son:",int(d))
else:
    print("uch xonali son emas boshqa son yozing!")