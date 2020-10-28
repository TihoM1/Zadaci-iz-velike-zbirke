""" 
Na osnovu stranice a kvadrata, stampati povrsinu i obim.
"""
def povrsina_obim(A):
    return A**2,A*4

a=int(input('a = '))
print("P, O = ", povrsina_obim(a))