while True:
    savol=input("Yaxshi korgan kitobingizni kiriting (toxtatmoqchi bolsangiz 'stop' deb yozing): ")
    if savol=="stop":
        break

while True:
    yosh=input("Yoshingizni kiriting(chiqmoqchi bolsangiz 'exit' yoki 'quit' deb yozing): ")
    if int(yosh)<=7:
       narx=2000
    elif int(yosh)>7 and int(yosh)<18:
        narx=3000
    elif int(yosh)>=18 and int(yosh)<65:
        narx=10000
    elif int(yosh)>=65:
        narx=0
    print(f"Siz uchun chipta narxi {narx} som")
    savol=input("Yana kitob qoshasizmi(ha/yoq)")
    if savol == "ha":
      continue
    else:
        break


yashik=[]
while True:
    mahsulot=input("Mahsulot kiriting: ")
    print("Mahsulot qabul qilindi")
    yashik.append(mahsulot)
    savol=input("Yana mahsulot qoshasizmi(ha/yoq)?")
    if savol == "ha":
        continue
    else:
        break
print("Sizning mahsulotlaringgiz ro'yxati")
print(yashik)


mahsulotlar={}
while True:
    mahsulot=input("Mahsulot kiriting: ")
    narx=int(input("Mahsulotni narxini kiriting: "))
    mahsulotlar[mahsulot] = narx
    savol=input("Yana mahsulot qoshasizmi(ha/yoq)?")
    if savol == "ha":
        continue
    else:
        break
print(mahsulotlar)