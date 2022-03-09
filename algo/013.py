# m massali jismga a tezlanish 
# berilganda qancha kuch tasir qiladi.
m=int(input("Jism massasini kiriting= "))
a=int(input("Jismga berilgan tezlanishni kiriting= "))
if(((1<=m)and(1<=a)) and ((m<=100)and(a<=100))):
    print("Jismga ta'sir qilgan kuch= ", m*a)
else:
    print("Kiritilgan son qo'yilgan shartga to'g'iri kelmadi. Boshqa son kiriting!")