import math
"""
Jednokraki trougao se oko visine spustene na osnvicu.
Izracunati povrsinu i zapreminu
"""
def povrsina_tijela(kateta_a,kateta_b):
    poluprecnik=kateta_b/2
    izvodnica=kateta_a
    povrsina=poluprecnik*math.pi*(poluprecnik+izvodnica)
    return povrsina

def zapremina_tijela(kateta_a,kateta_b):
    poluprecnik = kateta_b/2
    visina=math.sqrt(kateta_b**2-(kateta_a**2)/2)
    zapremina=(poluprecnik**2*math.pi*visina)/3
    return zapremina

a=int(input('Unesite krak trougla: '))
b=int(input('Unesite osnovicu trougla: '))
print("Povrsina tijela iznosi: ", povrsina_tijela(a,b))
print("Zapremina tijela iznosi: ", zapremina_tijela(a,b))