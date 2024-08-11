import math
def ildiz(son):
    x=math.sqrt(int(son))
    return x
son=input()
print(ildiz(son))

def daraja(son1,son2):
    x=pow(son1,son2)
    return x
son1,son2=map(int,input().split())
print(daraja(son1,son2))

import math
def gradus(burchak):
    x=math.radians(burchak)
    y=math.sin(x)
    return y
burchak=int(input())
print(gradus(burchak))

import random
def oraliq(son1,son2):
    x=random.randint(son1,son2)
    return x
son1,son2=map(int,input().split())
print(oraliq(son1,son2))

import random
mashinalar = ["Audi",'KIA',"BMW","Mers","Bugatti","Ferrari","Tesla"]
print(random.choice(mashinalar))