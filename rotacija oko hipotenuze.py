import math
"""
Program koji racuna povrsinu i zapreminu tijela 
koje nastaje rotacijom oko hipotenuze pravouglog trougla.
"""
def povrsina_tijela(kateta_a,kateta_b):
    hipotenuza=math.sqrt(kateta_a**2+kateta_b**2)
    povrsina=(kateta_a*kateta_b)/hipotenuza*3.14*(kateta_a+kateta_b)
    return povrsina

def zapremina_tijela(kateta_a,kateta_b):
    hipotenuza=math.sqrt(kateta_a**2+kateta_b**2)
    zapremina=(kateta_a**2*kateta_b**2*3.14)/(3*hipotenuza)
    return zapremina

a=int(input('Unesite vecu katetu: '))
b=int(input('Unesite manju katetu: '))
print("Povrsina tijela je: ", povrsina_tijela(a,b))
print("Zapremina tijla je: ", zapremina_tijela(a,b))