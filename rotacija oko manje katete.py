
"""
Izracunati povrsinu i zapreminu tijela koja se dobija 
rotacijom tijela oko manje katete. (a<b)
"""
import math

def povrsina_zapremina_tijela(kateta_a,kateta_b):
    poluprecnik=kateta_b
    izvodnica=math.sqrt(kateta_a**2+kateta_b**2)
    visina=kateta_a
    povrsina_tijela=poluprecnik**2*3.14+poluprecnik*3.14*izvodnica
    zapremina_tijela=(poluprecnik**2*visina*3.14)/3
    return povrsina_tijela, zapremina_tijela

a=int(input('Unesite vecu katetu: '))
b=int(input('Unesite manju katetu: '))
print(povrsina_zapremina_tijela(a,b))

