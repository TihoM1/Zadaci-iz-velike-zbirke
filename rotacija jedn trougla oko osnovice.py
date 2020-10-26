import math
"""
Jednakokraki trougao se okrece oko svoje osnove. 
Izracunati povrsinu i zapreminu tijela dobijenog 
pri rotaciji.
"""
def zapremina_tijela(kateta_a,kateta_b):
    poluprecnik=math.sqrt(kateta_b**2-(kateta_a**2)/2)
    visina=kateta_b
    zapremina=1/3*math.pi*poluprecnik*visina
    return zapremina

def povrsina_tijela(kateta_a,kateta_b):
    poluprecnik= math.sqrt(kateta_b**2-(kateta_a**2)/2)
    povrsina=math.pi*poluprecnik*(2*kateta_a)
    return povrsina

a=int(input('Unesite krak trougla: '))
b=int(input('Unesite osnovicu trougla: '))
print("Zapremina tijela iznosi: ",zapremina_tijela(a,b))
print("Povrsina tijela iznosi: ", povrsina_tijela(a,b))
