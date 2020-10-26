import math
"""
Izracunati povrsinu i zapreminu tijela koje se 
dobija rotacijom tijela oko vece osnove pravouglog
trapeza:
a - veca osnovica
b - manja osnovica
c - veci krak
d - manji krak
"""
def zapremina_tijela(osnovica_a, osnovica_b, krak_c, krak_d):
    poluprecnik = math.sqrt(krak_c**2-((a-b)/2)**2)
    zapremina_valjka = math.pi*poluprecnik*osnovica_b
    zapremina_kupe = (math.pi*poluprecnik**2*(a-b))/3
    return zapremina_kupe+zapremina_valjka

def povrsina_tijela(osnovica_a, osnovica_b, krak_c, krak_d):
    poluprecnik = math.sqrt(krak_c**2-((a-b)/2)**2)
    povrsina_valjka = math.pi*poluprecnik**2+2*math.pi*poluprecnik*osnovica_b
    povrsina_kupe = krak_c*poluprecnik*math.pi
    return povrsina_valjka+povrsina_kupe

a=int(input('Unesite duzu osnovicu: '))
b=int(input('Unesite kracu osnovicu: '))
c=int(input('Unesite duzi krak: '))
d=int(input('Unesite kraci krak: '))
print('Zapremina tijela je: ', zapremina_tijela(a,b,c,d))
print('Povrsina tijela je:', povrsina_tijela(a,b,c,d))
