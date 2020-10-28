"""
Date su stranice a i b pravougaonika.
Stampati povrsinu i obim.
"""
def povrsina_obim(A,B):
    return A*B,A*2+B*2

a=int(input('a = '))
b=int(input('b = '))
print('P, O = ', povrsina_obim(a,b))