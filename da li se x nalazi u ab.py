"""
Napisati kod koji učitava brojeve x, a i b 
provjerava da li x pripada intervalu [a,b] i štampa
odgovarajuću poruku („Pripada“ ili „Ne pripada“). 
x=10, a=1 , b=55 -> Pripada
x=60, a=0 , b=10 -> Ne pripada
"""
def da_li_pripada(x,a,b):
    return (x>=a and x<=b)

X=int(input('x = '))
A=int(input('a = '))
B=int(input('b = '))
true_false= da_li_pripada(X,A,B)
if true_false:
    print('Pripada')
else:
    print('Ne pripada')