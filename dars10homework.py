def kopaytma(*sonlar):
    a=1
    for i in sonlar:
        a*=i
    return a
print(kopaytma(1,2,3,234,23))


def talabalar(ism,familya,**malumotlar):
    malumotlar["ism"]=ism
    malumotlar["familya"]=familya
    return malumotlar
print(talabalar("Siroj","Jumanazarov",fakulitet="fizika"))
