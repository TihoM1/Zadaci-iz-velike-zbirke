"""
Napisati metod koji učitava cijele brojeve, sve dok se ne učita
cio broj koji je veći od x, a zatim štampa broj učitanih brojeva, 
broj učitanih parnih brojeva i zbir svih učitanih brojeva. 
"""

def parni_neparni(n):
    i = 1
    n_parnih=0
    n_neparnih=0
    while  n >= i:
        if i % 2 == 0:
            n_parnih+=1
        else:
            n_neparnih+=1
        i+=1
    return n_parnih , n_neparnih

N=int(input())
print(parni_neparni(N))
