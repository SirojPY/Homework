import random
class User:
    """Foydalanuvchi akcountini malumotlari"""
    def __init__(self,ism,familya,tyil):
        """Foydalanuvchi malumotlari"""
        self.ism=ism
        self.familya=familya
        self.tyil=tyil
    def get_name(self):
        """Foydalanuvchi ismini qaytaradi"""
        x=(self.ism).capitalize()
        return x
    def get_user(self):
        """Foydalanuvchi familyasini qaytaradi"""
        y=(self.familya).capitalize()
        return y
    def get_email(self):
        """Foydalanuvchi emailini qaytaradi"""
        sonlar=random.randint(0,100)
        z=f"{(self.ism).capitalize()}{(self.familya).lower()}{sonlar}@gmail.com"
        return z
    def get_age(self):
        """Foydalanuvchi yoshini qaytaradi"""
        return 2024-self.tyil

user1=User("Siroj","Jumanazarov",2009)
user2=User("Hasan","Husanov",2000)

print(user1.get_email())
print(user2.get_email())


