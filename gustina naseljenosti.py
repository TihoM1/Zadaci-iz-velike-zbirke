"""
Na osnovu povrsine drzave i broja stanovnika 
stampati gustinu naseljenosti.
"""
def gustina(povrsina_d, br_st):
    return br_st/povrsina_d

p=int(input('Povrsina drzave je: '))
n=int(input('Broj stanovnika je: '))
print('Gustina naseljenosti je: ',round(gustina(p,n),1),'st/km^2')