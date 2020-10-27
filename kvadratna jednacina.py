"""
Kod koji provjerava da li kvadratna jednacina
ax^2+bx+c=0 ima realna rjesenja.
Npr. 2x^2-4x+4=0 nema realna rjesnja
6x^2 + 11x - 35 = 0 ima realna rjesenja
"""
def da_li_ima_realna_rjesenja(a,b,c):
    if 2*a!=0 and b**2-4*a*c>=0:
        return True
    return False

A=int(input('a = '))
B=int(input('b = '))
C=int(input('c = '))
print(da_li_ima_realna_rjesenja(A,B,C))