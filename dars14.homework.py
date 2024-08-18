class Avto():
    def __init__(self,model,rang,karobka,narx):
        """Avtoning xususiyatlari"""
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.km = 0
    def avto_info(self):
        return f"model:{self.model},rangi:{self.rang},karobka:{self.karobka},narxi:{self.narx}$,km:{self.km}"
    def set_km(self,km):
        """Avto ning km sini yangilovchi metod"""
        self.km = km
    def update_km(self):
        """Km ni 10000 ga kopaytirish"""
        self.km +=10000
# avto1=Avto("kaptiva","qora","avto","20000")
# avto1.update_km()
# avto1.update_km()
# avto1.update_km()
# print(avto1.avto_info())
class Avtosalon():
    """Avtosalon xususiyatlari"""
    def __init__(self,nomi,manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar_soni=0
        self.sotuvdagi_avtolar=[]
    def add_avto(self,avto):
        """Avto salonga avto qoshish"""
        self.sotuvdagi_avtolar.append(avto)
        self.avtolar_soni+=1
mashinalar=Avtosalon("GM","Toshkent")
avto1=Avto("kaptiva","qora","avto","20000")
avto2=Avto("gentra","oq","mexanik","10000")
avto3=Avto("nexia 2","qora","mexanik","9000")

# mashinalar.add_avto(avto1)
# mashinalar.add_avto(avto2)
# mashinalar.add_avto(avto3)
# print(mashinalar.avtolar_soni)

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Avto))

print(see_methods(Avtosalon))

print(see_methods(avto1))

print(avto1.__dict__)

print(avto1.__dict__.keys())



