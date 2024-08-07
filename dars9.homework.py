def yosh_top(ism,t_yil, yosh=2024):
    """Foydalanuvchini yoshini topib beruvchi dastur"""
    yosh_hisobi=f"{ism} ning yoshi {yosh-t_yil} da"
    return yosh_hisobi
print(f"{yosh_top("siroj", 2009)}")

def son_kv(son,kv=2,kub=3):
    """Kvadrat va kub topuvchi dastur"""
    kub1=(f"{son} nining kvadrati {son**kv} ga teng\n"
        f"{son} nining kubi {son**kub} ga teng")
    return kub1
print(son_kv(12))

def son(son):
    """Sonni juft yoki toqlikini biuvchi funksiya"""
    if son%2==0:
        g="juft"
    else:
        g="toq"
    return g
print(f"Bu son {son(2)}")

def sonlar(a,b):
    """Sonlardan kattasini topib beruvchi dastur"""
    if a==b:
        f="Sonlar teng"
    else:
        f=max(a,b)
    return f
print(sonlar(12,13))

def sonlar(a,b):
    """Sonlarni darajasini topuvchi dastur"""
    d=f"{a} ning {b} chi darajasi {a**b}"
    return d
print(sonlar(12,13))

def sonlar(son):
    """Sonlarni boluvchilar sonini topib beruvchi dastur"""
    b=2
    q=0
    while b<11:
        if son%b==0:
            q+=1
        b+=1
    return q
print(f"Bo'luvchilar soni ga {sonlar(88)} teng")







