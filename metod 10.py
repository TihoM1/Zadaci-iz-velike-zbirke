"""
Napisati metod koji vraća zbir najveće i najmanje cifre broja
n.
"""
def zbir_max_i_min_cifre(n):
    d=[]
    while n>0:
            d.append(n % 10)
            n//=10
    return max(d) + min(d)

n=int(input('n = '))
print("Zbir max i min cifre:",zbir_max_i_min_cifre(n))