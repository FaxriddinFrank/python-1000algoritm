n=int(input("uch xonali son kiriting:"))
a=n//100
b=(n//10)%10
c=n%10
d=(c*100)+(b*10)+a
if((n<1001) and (n>99)):
    print("teskari soni",int(d),"ga teng")
else:
    print("uch xonali son emas boshqa son kiriting")