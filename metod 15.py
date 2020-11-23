"""
Napisati metod koji vraća najmanji prirodan broj k
takav da n nije veći od broja 2k:
n = 7 -> k = 3 jer 2^3 > 7
n = 8 -> k = 5 ker 2^4 > 8
"""
def min_k(n):
    k=1
    while k>0:
        if 2**k >n:
            return k
        else:
            pass
        k+=1
    
N=int(input("Unesite br. n: "))
print("2^" + str(min_k(N)), ">", N)