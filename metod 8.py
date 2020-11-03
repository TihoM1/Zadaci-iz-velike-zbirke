"""
 Napisati metod koji vraća zbir cifara broja n. 
"""
def zbir_cifara_broja_n(n):
    zbir=0
    while n>0:
        zbir+=n%10
        n//=10
    return zbir

n=int(input('n = '))
print('Zbir cifara broja n iznosi:',zbir_cifara_broja_n(n))
