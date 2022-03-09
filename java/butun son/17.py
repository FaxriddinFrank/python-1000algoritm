n=int(input("999 dan katta bo'lgan sonni kiriting= "))
a=(n%1000)//100
if(n>999):
    print("Berilgan sonning yuzlar xonasidagi son= ", a)
else:
    print("Kiritilgan son 999 dan kichkina. Qaytadan son kiriting!")