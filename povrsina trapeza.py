"""
Date su str. a i b i hipotenuza h.
Stampati povrsinu trapeza.
"""
def povrsina(A,B,H):
    return ((A+B)*H)/2

a=int(input('a = '))
b=int(input('b = '))
h=int(input('h = '))
print('Povrsina iznosi: ', povrsina(a,b,h))