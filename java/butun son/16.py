n=int(input("uch xonali son:"))
a=(n//10)%10
b=n//100
d=n%10
c=(b*100)+(d*10)+a
if((n<1000)and(n>99)):
    print("hosil bo'lgan son:",int(c))
else:
    print("uch xonali son emas, boshqa son kiriting!")