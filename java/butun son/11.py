n=int(input("uch xonali son kiriting:"))
a=n%10
b=(n//10)%10
d=n//100
if((n>99) and (n<1001)):
    print("sonlar yig'indisi :",int(a)+int(b)+int(d),"ga teng.")
else:
    print("uch xonali son emas, boshqa son kiriting")