"""
Napisati metod koji vraća x^n.
Ne koristiti metod pow iz klase Math. 
"""
def poww(x,n):
    return x**n

x=int(input('Baza: '))
n=int(input('Eksponent: '))
print(poww(x,n))