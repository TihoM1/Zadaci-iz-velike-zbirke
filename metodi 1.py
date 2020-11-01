"""
Napisati metod koji vraća broj a*x, ako je
x nenegativan i a/x, ako je x negativan. 
"""
def poz_ili_neg(X):
    if X>0:
        return True
    else: 
        return False

def rezultat(A,poz_ili_neg_x,X):
    if poz_ili_neg_x:
        return A*X
    else:
        return A/X

a=int(input('a = '))
x=int(input('x = '))
print(rezultat(a,poz_ili_neg(x),x))