"""
Napisati metod koji vraća n! (n! = 1*2*...*n).
"""
def factorijel(n):
    if n == 1:
       return n
    else:
       return n*factorijel(n-1)

n=int(input('n = '))
print("n! =",factorijel(n))