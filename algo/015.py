# Zanjirning R1, R2 va R3 qarshiliklari o'zaro parallel ulangan. 
# Ularning umumiy qarshiligini toping. 
R1=float(input("Zanjirning birinchi qarshiligini kiriting= "))
R2=float(input("Zanjirning ikkinchi qarshiligini kiriting= "))
R3=float(input("Zanjirning uchunchi qarshiligini kiriting= "))
if(((1<=R1)and(1<=R2) and (1<=R3)) and ((R1<=100)and(R2<=100) and (R3<=100))):
    print("Zanjirning umumiy qarshiligi= ", (R1*R2*R3)/(R3*R2+R1*R3+R1*R2))
else:
    print("Kiritilgan son qo'yilgan shartga to'g'iri kelmaydi. Boshqa son kiriting!")