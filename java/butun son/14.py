n=int(input("uch xonali son kiriting:"))
a=n%10
b=n//10
d=(a*100)+b
if(n>99 and n<1000):
    print("Raqamlari yig'indisi= ", d)
else:
    print("Kiritilgan son uch xonali son emas. Qaytadan son kiriting!")